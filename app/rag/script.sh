#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

DB_NAME="$1"
VECTOR_DB_DIR="$(dirname "$DB_NAME")/vector_db"
mkdir -p "$VECTOR_DB_DIR"

sqlite3 $DB_NAME <<EOF
.mode csv
.headers on
.output "$VECTOR_DB_DIR/tables.csv"
SELECT name FROM sqlite_master WHERE type='table';
EOF

for table in $(sqlite3 $DB_NAME .tables); do
    sqlite3 $DB_NAME <<EOF
.mode csv
.headers on
.output "$VECTOR_DB_DIR/$table.csv"
SELECT * FROM $table;
EOF
done