# TODO.md

- [x] **Install MySQL**: If you haven't done this yet, follow this [Guide](https://ahmedsalim3.github.io/posts/install-mysql-on-linux/) if you're on Linux. For Windows, refer to the [Docs](https://dev.mysql.com/doc/refman/8.4/en/windows-installation.html).

- [x] **Start the MySQL Service**:

    ```sh
    sudo systemctl start mysql
    ```

- [x] **Update Database Configuration**: Run the [`MySQLDatabaseManager`](./csv2mysql.py) class to create the database and populate the tables with the data.

    ```sh
    cd rdbms/
    python csv2mysql.py # Ensure you're in the ~/rdbms/ directory
    
    python -m rdbms.csv2mysql # Alternatively, run this from the main project root
    ```

- [ ] **Access the Database**: After creating the database, you can access it using [MySQL Workbench][mysql-workbench], [phpMyAdmin][php-my-admin], or other tools.

    It's advisable to set up a new MySQL user and grant that user full privileges on the database for better security.
    
    - [ ] **Open a terminal and log in**:

        ```sh
        mysql -u root -p # Replace 'root' with your username and enter your password
        ```
    
    - [ ] **Verify that the database was created**:
        ```sql
        SHOW DATABASES;
        ```

    - [ ] **Create a new user** with the desired `USERNAME`, `HOSTNAME`, and `PASSWORD`:

        ```sql
        CREATE USER 'USERNAME'@'%' IDENTIFIED BY 'PASSWORD';
        GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'%' WITH GRANT OPTION;
        FLUSH PRIVILEGES;
        ```
        _Note: The `%` allows connections from any host._
    
    - [ ] **To view all users**, run:

        ```sql
        SELECT user, host FROM mysql.user;
        ```

- [ ] **Access the Database from MySQL Workbench**:

Log in with the new user credentials created earlier. If you’re on the same machine, you can use `localhost` as the hostname. For a different machine, use the IP address, as the `USERNAME` user accepts connections from any host due to the `%` in the `HOSTNAME`. You might need to modify the MySQL configuration file (`mysqld.cnf`).

- [ ] **Find your IP Address**:

    ```sh
    hostname -I
    ```

- [ ] **Modify the `bind-address`** in the MySQL configuration file:

    ```sh
    sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
    ```

    - Look for `bind-address`. If it's set to `127.0.0.1`, MySQL will only accept local connections.
    - Change it to `0.0.0.0` or comment it out to allow connections from any IP address.

- [ ] **Restart the MySQL Service** and verify changes:

    ```sh
    sudo systemctl restart mysql
    ```

- [ ] **Snapshots**: Below is an example showing how we connected via MySQL Workbench.


- [x] **Show Database Name**:
    ```sql
    SHOW DATABASES;
    EXIT;
    ```

- [x] **Dump and Export MySQL Database** into a directory:

    ```sh
    cd rdbms/
    mysqldump --skip-extended-insert --compact -u root -p adventureworks > DUMP_adventureworks.sql
    ```

- [x] **Convert MySQL Database to SQLite**: Follow the guides in [mysql2sqlite](./mysql2sqlite/README.md). Run:

    ```sh
    ./mysql2sqlite/mysql2sqlite DUMP_adventureworks.sql | sqlite3 adventureworks.db
    ```

- [x] **Run `utils.py` to view the database table info**

    ```sh
    python utils.py 
    ```

[mysql-workbench]: https://www.mysql.com/products/workbench/
[php-my-admin]: https://www.phpmyadmin.net/