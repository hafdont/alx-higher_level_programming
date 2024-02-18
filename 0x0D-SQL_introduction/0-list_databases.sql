#!/usr/bin/env bash

# MySQL credentials
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

# Use mysql command to connect to MySQL server and execute SHOW DATABASES;
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"
