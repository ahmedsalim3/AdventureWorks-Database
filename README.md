# Adventureworks Database

This repository is for setting up a relational MySQL database in Python, building a Text-to-SQL Streamlit app that translates plain language questions into SQL queries, and executing those SQL queries on the database to retrieve results.

<p align= "center">
<img src="https://hits.sh/github.com/ahmedsalim3/AdventureWorks-Database/edit/main/app.svg?label=views&color=fe7d37">
<img src="https://img.shields.io/badge/PYTHON-3.9+-orange">
<img src="https://img.shields.io/badge/Apache-2.0 license--3.0-orange">
</p>

## How to setup the database?

In this [blog](https://ahmedsalim3.github.io/posts/adventureworks-database/), I cover the steps to create the database and convert it into SQLite. The [rdbms](./rdbms/) folder contains the code for this process. Refer to [TODO](./rdbms/TODO.md) for more details.

## Installation

1. **Clone this repository:**

  ```bash
  git clone https://github.com/ahmedsalim3/AdventureWorks-Database.git
  ```

2. **Navigate to the repository directory:**

  ```bash
  cd AdventureWorks-Database
  ```

3. **Create a Virtual Environment (Recommended):**

  ```bash
  python -m venv env
  .\env\Scripts\activate  # On Windows
  source env/bin/activate  # On macOS/Linux
  ```

4. **Install Requirements:**

  ```bash
  pip install -r requirements.txt
  ```

## Repo's directory structure

```sh
.
├── app                             <- Text-To-SQL Streamlit app
│   ├── README.md
│   ├── app.py
│   ├── config.py
│   ├── constants.py
│   ├── requirements.txt
│   └── ui
│ 
├── data                            <- Data source
│ 
├── rdbms                           <- Relational Database Management System
│   ├── DUMP_adventureworks.sql
│   ├── TODO.md
│   ├── __init__.py
│   ├── adventureworks.db
│   ├── adventureworks_schema.png
│   ├── assets
│   ├── csv2mysql.py
│   ├── install_mysql_linux.md
│   ├── mysql2sqlite
│   ├── schema.sql
│   └── utils.py
│ 
├── LICENSE
├── README.md
└── requirements.txt

```