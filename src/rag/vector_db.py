# pip install sqlite-vec google-generativeai
# https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/embed_content.md
# inspired from @ https://alexgarcia.xyz/sqlite-vec/python.html
# sourced from @ https://github.com/asg017/sqlite-vec/blob/main/examples/simple-python/demo.py

from src.rag.documents import SENTENCES, TABLES, SCHEMAS
from google.generativeai.embedding import embed_content
import sqlite3
import sqlite_vec
import struct
from typing import List
from src.config import EMBEDDING_MODEL
import logging

logging.basicConfig(level=logging.INFO)


class VectorDatabase:
    def __init__(self, db_path: str = ":memory:"):
        self.db = sqlite3.connect(db_path)
        self.db.enable_load_extension(True)
        sqlite_vec.load(self.db)
        self.db.enable_load_extension(False)

        self.create_tables()
        self.insert_sentences()

    @staticmethod
    def serialize(vector: List[float]) -> bytes:
        """serializes a list of floats into a compact "raw bytes" format"""
        return struct.pack("%sf" % len(vector), *vector)

    def create_tables(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS sentences (
              id INTEGER PRIMARY KEY,
              sentence TEXT,
              table_name TEXT,
              schema_definition TEXT
            );
            """
        )

        self.db.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS vec_sentences USING vec0(
              id INTEGER PRIMARY KEY,
              sentence_embedding FLOAT[768]
            );
            """
        )

    def insert_sentences(self):
        with self.db:
            for i, sentence in enumerate(SENTENCES):
                table_name = TABLES[i]
                schema_definition = SCHEMAS[i]
                self.db.execute(
                    "INSERT INTO sentences(id, sentence, table_name, schema_definition) VALUES(?, ?, ?, ?)",
                    [i, sentence, table_name, schema_definition],
                )

    def embed_sentences(self):
        with self.db:
            sentence_rows = self.db.execute(
                "SELECT id, sentence, table_name, schema_definition FROM sentences"
            ).fetchall()
            embeddings = embed_content(
                model=EMBEDDING_MODEL,
                content=[row[1] for row in sentence_rows],
                task_type="SEMANTIC_SIMILARITY",
            )["embedding"]

            logging.info(f"Number of sentence_rows: {len(sentence_rows)}")

            for (id, _, _, _), embedding in zip(sentence_rows, embeddings):
                self.db.execute(
                    "INSERT INTO vec_sentences(id, sentence_embedding) VALUES(?, ?)",
                    [id, self.serialize(embedding)],
                )

    def retrieval(self, query: str, k: int = 3):
        query_embedding = embed_content(
            model=EMBEDDING_MODEL,
            content=query,
            task_type="RETRIEVAL_DOCUMENT",
            title="Return",
        )["embedding"]

        results = self.db.execute(
            """
            SELECT
              vec_sentences.id,
              distance,
              sentences.sentence,
              sentences.table_name,
              sentences.schema_definition
            FROM vec_sentences
            LEFT JOIN sentences ON sentences.id = vec_sentences.id
            WHERE sentence_embedding MATCH ? 
              AND k = ?
            ORDER BY distance
            """,
            [self.serialize(query_embedding), k],
        ).fetchall()

        logging.info(f"Number of retrievals: {len(results)}")

        return results


# # # Example
# if __name__ == "__main__":
#     db = VectorDatabase('rag/example/example.db')
#     db.embed_sentences()
#     # retrieve the top 3 results based on the query
#     results = db.retrieval("how many items were returned in 2024?", 5)
#     for i, row in enumerate(results):
#         index = results[i][0]
#         distance = results[i][1]
#         sentence = results[i][2]
#         table_name = results[i][3]
#         table_schema = results[i][4]
#         # print details of the first retrieval
#         if i == 0:
#             print(f'First table matched: {table_name}, Distance {distance}')
#             print(sentence)
