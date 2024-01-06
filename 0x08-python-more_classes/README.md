Project: 0x08 Python - More Classes and Objects
Requirements:
All files are interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5).
All files end with a new line.
The first line of all files is #!/usr/bin/python3.
A README.md file, at the root of the project folder, is mandatory.
Code follows PEP 8 style (using pycodestyle, version 2.8.*).
All files must be executable.
Tasks
0. Simple Rectangle
File: 0-rectangle.py
An empty class Rectangle is defined.
1. Real definition of a rectangle
File: 1-rectangle.py
Defines a Rectangle class with private instance attributes width and height.
Includes getters and setters for both attributes.
Instantiates with optional width and height.
2. Area and Perimeter
File: 2-rectangle.py
Extends the Rectangle class from task 1.
Adds public methods area and perimeter to calculate area and perimeter.
3. String representation
File: 3-rectangle.py
Extends the Rectangle class from task 2.
Updates the Rectangle class to include a string representation.
4. Eval is magic
File: 4-rectangle.py
Extends the Rectangle class from task 3.
Adds the __repr__ method to the Rectangle class for a string representation that can recreate an instance.
5. Detect instance deletion
File: 5-rectangle.py
Extends the Rectangle class from task 4.
Adds a __del__ method to print a message when an instance is deleted.
6. How many instances
File: 6-rectangle.py
Extends the Rectangle class from task 5.
Adds a public class attribute number_of_instances to keep track of the number of instances.
7. Change representation
File: 7-rectangle.py
Extends the Rectangle class from task 6.
Adds a public class attribute print_symbol to change the default string representation character.
8. Compare rectangles
File: 8-rectangle.py
Extends the Rectangle class from task 7.
Adds a static method bigger_or_equal to compare two rectangles based on area.
9. A square is a rectangle
File: 9-rectangle.py
Extends the Rectangle class from task 8.
Adds a class method square to create a new instance representing a square.
10. N queens (Advanced)
File: 101-nqueens.py
Solves the N queens problem for a given N using backtracking.
Prints every possible solution with one solution per line.
Usage Instructions
Task 10 - N Queens
Run the following command in the terminal:

./101-nqueens.py N
Replace N with the desired value (an integer greater or equal to 4).

Example:
./101-nqueens.py 4

Output:
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]


Author
Hafiz Yusuf. 
