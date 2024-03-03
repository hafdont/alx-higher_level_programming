# SQL - More Queries

This project is a collection of SQL scripts that perform various tasks related to managing MySQL databases. The scripts cover a range of topics including user privileges, database creation, table creation, and data retrieval.

## Project Description

This project contains SQL scripts that address the following tasks:

1. **My Privileges**: Script to list all privileges of MySQL users.
2. **Root User**: Script to create a MySQL server user with all privileges.
3. **Read User**: Script to create a database and a user with only SELECT privilege.
4. **Always a Name**: Script to create a table with a non-null name field.
5. **ID Can't Be Null**: Script to create a table with a non-null ID field.
6. **Unique ID**: Script to create a table with a unique ID field.
7. **States Table**: Script to create a database and a table for states.
8. **Cities Table**: Script to create a database and a table for cities with a foreign key constraint.
9. **Cities of California**: Script to list all cities in California without using JOIN.
10. **Genre ID by Show**: Script to list shows with at least one genre linked.
11. **Genre ID for All Shows**: Script to list all shows and their genres.
12. **No Genre**: Script to list shows without a genre linked.
13. **Number of Shows by Genre**: Script to list genres and the number of shows linked to each.
14. **My Genres**: Script to list genres of a specific show.
15. **Only Comedy**: Script to list all comedy shows.
16. **List Shows and Genres**: Script to list all shows and their genres.
17. **Not My Genre**: Script to list genres not linked to a specific show.
18. **No Comedy Tonight!**: Advanced script to list genres without comedy shows.

## Getting Started

To run the scripts, you need to have MySQL installed on your system. You can install MySQL on Ubuntu 20.04 LTS using the following commands:

```bash
$ sudo apt update
$ sudo apt install mysql-server

Once MySQL is installed, you can connect to the MySQL server using the mysql command:

$ mysql -uroot -p


Then, you can execute the SQL scripts using the mysql command with the appropriate options.

Usage
Each SQL script is designed to be executed using the mysql command-line tool. For example, to execute the script 0-privileges.sql, you can use the following command

$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p


Replace 0-privileges.sql with the name of the script you want to execute.

License
This project is licensed under the MIT License. See the LICENSE file for details.


This README.md file provides an overview of the project, including its description, how to get started, usage instructions, and licensing information. You can add this file to the root directory of your project. Let me know if you need further assistance!

