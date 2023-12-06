Python Hello World Project
This repository contains a collection of Python scripts and programs that cover various fundamental concepts and tasks. The scripts range from basic print statements to more advanced topics like working with linked lists and bytecode.

Project Structure
The project is organized into several directories, each containing Python scripts related to specific tasks:

0-run: Shell script for running a Python script specified in the environment variable $PYFILE.

Example: ./0-run
1-run_inline: Shell script for running Python code specified in the environment variable $PYCODE.

Example: ./1-run_inline
2-print.py: Python script that prints a specific string using the print function.

Example: ./2-print.py
3-print_number.py: Python script to print an integer stored in a variable, followed by a string.

Example: ./3-print_number.py
4-print_float.py: Python script to print a float with a precision of 2 digits.

Example: ./4-print_float.py
5-print_string.py: Python script to print a string three times followed by its first 9 characters.

Example: ./5-print_string.py
6-concat.py: Python script to concatenate strings and print a specific message.

Example: ./6-concat.py
7-edges.py: Python script to extract and print specific portions of a string.

Example: ./7-edges.py
8-concat_edges.py: Python script to print a new sentence by concatenating specific portions of a string.

Example: ./8-concat_edges.py
9-easter_egg.py: Python script to print "The Zen of Python" by Tim Peters.

Example: ./9-easter_egg.py
10-check_cycle.c: C program to check if a singly linked list has a cycle.

Example: ./cycle
100-write.py: Python script to print a specific message to stderr and exit with status code 1.

Example: ./100-write.py
101-compile: Shell script to compile a Python script file specified in the environment variable $PYFILE.

Example: ./101-compile
102-magic_calculation.py: Python function magic_calculation(a, b) designed to match specific Python bytecode.

Usage Instructions
For each script or program, refer to the provided examples for usage instructions. Additionally, some scripts may require specific environment variables, as indicated in the corresponding section.

Questions List
0. How to create a Shell script that runs a Python script specified in an environment variable?

1. How to create a Shell script that runs inline Python code specified in an environment variable?

2. How to print a specific string using the print function in Python?

3. How to print an integer stored in a variable followed by a string without casting the variable into a string?

4. How to print a float with a precision of 2 digits without casting the variable into a string?

5. How to print a string three times followed by its first 9 characters without using loops or conditional statements?

6. How to concatenate strings and print a specific message without using loops or conditional statements?

7. How to extract and print specific portions of a string without using loops or conditional statements?

8. How to concatenate specific portions of a string and print a new sentence without creating new variables or using string literals?

9. How to print "The Zen of Python" by Tim Peters using a Python script within a specific character limit?

10. How to check if a singly linked list has a cycle in C without using certain functions?

  
The solution uses Floyd's Cycle Detection Algorithm, also known as the "tortoise and hare" algorithm. The basic idea is to have two pointers traverse the list at different speeds. If there is a cycle, the faster pointer will eventually catch up to the slower pointer.

Here is a step-by-step breakdown of the solution:

Two pointers (slow and fast) are initialized to the head of the linked list.
In each iteration, the slow pointer moves one step, and the fast pointer moves two steps.
If there is no cycle, the fast pointer will eventually reach the end of the list, and the function returns 0.
If there is a cycle, the fast pointer will catch up to the slow pointer, and the function returns 1.

11. How to print a specific message to stderr in Python and exit with status code 1 without using print?
12.  How to create a Shell script to compile a Python script file specified in an environment variable?
13. How to write a Python function magic_calculation(a, b) that matches specific Python bytecode?
