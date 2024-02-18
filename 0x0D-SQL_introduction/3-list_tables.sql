#!/bin/bash

# Check if the database name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Store the database name from the argument
db_name="$1"

# Use mysql command to list all tables in the specified database
mysql -uroot -proot -e "USE $db_name; SHOW TABLES;"
