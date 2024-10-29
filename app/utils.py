import sqlite3


def execute_sql_query(sql, db_path):
    """Execute SQL query and return results along with column names and error (if any)."""
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            col_names = [desc[0] for desc in cur.description]
            return rows, col_names, None
    except sqlite3.Error as e:
        return None, None, str(e)


def create_rag_prompt(number_of_retrieval, retrieval, schema_info, top_k):
    """Creates a RAG prompt based on retrieved data, schema, and instructions."""
    table_info = ", ".join([row[3] for row in retrieval])
    sentence_info = "\n".join([row[2] for row in retrieval])

    return (
        "You are a SQL expert. Given an input question, generate a syntactically correct SQL query to execute, returning ONLY the generated query. Unless specified, limit the output to {top_k} rows.\n\n"
        "**Target Tables**: Focus on the top {number_of_retrieval} tables from the Vector Database: '{table_info}'.\n\n"
        "**Contextual Information**:\n"
        "{sentence_info}\n\n"
        "**Schema Overview**:\n"
        "{schema_info}\n\n"
        "**Instructions for Query Creation**:\n"
        "- Ensure the columns queried exist in the tables and use aliases only when necessary.\n"
        "- **Use Only Defined Schema**: Reference only the tables and columns specified in the schema."
        "- Always utilize SQLite-compatible date functions like `strftime('%Y', OrderDate)` for date manipulations.\n"
        "- For multiple conditions, effectively use logical operators (AND, OR).\n"
        "- Apply appropriate SQLite functions for date arithmetic and extractions.\n"
        "- Use GROUP BY with aggregate functions for any required data grouping.\n"
        "- Enhance readability with aliases for tables and columns in complex joins or subqueries.\n"
        "- Employ subqueries or common table expressions (CTEs) as needed to simplify queries.\n"
        "- Note that the database holds data only until 2017.\n\n"
        "**Example Queries**:\n\n"
        "1. Find the 10 cheapest products in ascending order:\n"
        "SELECT ProductName, ProductPrice FROM products ORDER BY ProductPrice ASC LIMIT 10;\n"
        "2. Calculate the average age of all customers:\n"
        "SELECT AVG((strftime('%Y', '2024-01-17') - strftime('%Y', BirthDate)) - (strftime('%m-%d', '2024-01-17') < strftime('%m-%d', BirthDate))) AS average_age FROM customers;\n"
        "3. List all customers whose annual income is less than 20,000 and who bought products in 2015:\n"
        "SELECT FirstName, LastName, AnnualIncome, ProductName, YEAR(OrderDate) AS Year FROM sales_2015 JOIN products ON sales_2015.ProductKey = products.ProductKey JOIN customers ON sales_2015.CustomerKey = customers.CustomerKey WHERE AnnualIncome < 20000;"
    ).format(
        number_of_retrieval=number_of_retrieval,
        table_info=table_info,
        schema_info=schema_info,
        sentence_info=sentence_info,
        top_k=top_k,
    )


def format_answer_prompt(question, query, result):
    """Formats the prompt to get a final answer from the model based on SQL results."""
    return (
        "Given the following user question, corresponding SQL query, and SQL result, answer the user question.\n\n"
        "Reply with the user's language."
        "Question: {question}\n"
        "SQL Query: {query}\n"
        "SQL Result: {result}\n"
        "Answer: "
    ).format(question=question, query=query, result=result)
