# Install MySQL on linux via terminal
This guide will help you install and configure MySQL on a Linux system.

If MySQL is already installed, you will need to clean up the previous installations:

<details>
<summary><b>Clean Up Existing MySQL Installation</b></summary>

- [ ] Completely removing MySQL and its related packages from your system

    ```sh
    sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
    sudo apt-get autoremove
    sudo apt-get autoclean
    ```

- [ ] Set up MySQL directories and permissions

    ```sh
    sudo mkdir -p /var/lib/mysql
    sudo mkdir -p /var/run/mysqld
    sudo chown -R mysql:mysql /var/lib/mysql
    sudo chown -R mysql:mysql /var/run/mysqld
    sudo chmod 750 /var/run/mysqld
    ```

</details> 

## Install MySQL

- [x] Update your package lists and install MySQL

    ```sh
    sudo apt-get update
    sudo apt-get install mysql-server
    ```

- [x] Initialize MySQL

    ```sh
    sudo mysqld --initialize --user=mysql --datadir=/var/lib/mysql
    ```

- [x] Start MySQL Service

    ```sh
    sudo systemctl start mysql
    ```

- [x] Check Status and Logs

    ```sh
    sudo systemctl status mysql
    ```

- [x] Secure the Installation

    ```sh
    sudo mysql_secure_installation
    ```

- [x] Log In with the temporary password

    ```sh
    sudo mysql -u root -p
    ```

**NOTE: The temporary password will be shown during the installation. If you missed it, you can find it in the logs:**

- [ ] Viewing MySQL error logs

    ```sh
    sudo less /var/log/mysql/error.log
    ```

_Look for a line that's similar to: `A temporary password is generated for root@localhost: TEMP_PASSWORD`_

If you stll can't find the temporary password, or if you need to reset it, follow these steps:

- [ ] Stop the MySQL service

    ```sh
    sudo systemctl stop mysql
    ```

- [ ] Start MySQL in safe mode

    ```sh
    sudo mysqld_safe --skip-grant-tables &
    ```

- [ ] If `/var/run/mysqld` doesn't exist, create it:
    
    ```sh
    sudo mkdir -p /var/run/mysqld
    sudo chown mysql:mysql /var/run/mysqld
    ```

- [ ] Log into MySQL without a password

    ```sh
    mysql -u root 
    ```

- [ ] Reset the root password:

    ```sql
    FLUSH PRIVILEGES;
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'PASSWORD'; # PASSWORD is your new pass
    EXIT;
    ```

- [ ] Stop MySQL safe mode:

    ```sh
    sudo killall mysqld_safe
    ```

- [ ] Restart MySQL:

    ```sh
    sudo systemctl start mysql
    ```

- [ ] Log in with the new password:

    ```sh
    mysql -u root -p
    ```

# References

[Install MySQL on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

[Ubuntu Server](https://ubuntu.com/server/docs/install-and-configure-a-mysql-server)