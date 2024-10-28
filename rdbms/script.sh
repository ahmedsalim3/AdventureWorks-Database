#!/bin/bash
mkdir db_tables

DB_NAME="adventureworks.db"
sqlite3 $DB_NAME <<EOF
.mode csv
.headers on
.output ./db_tables/tables.csv
SELECT name FROM sqlite_master WHERE type='table';
EOF

for table in $(sqlite3 $DB_NAME .tables); do
    sqlite3 $DB_NAME <<EOF
.mode csv
.headers on
.output ./db_tables/$table.csv
SELECT * FROM $table;
EOF
done
