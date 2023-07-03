# 0x08-python-more_classes

## Description

This project is a deep dive into Python classes and Object-Oriented Programming. It involves tasks related to class creation, instance methods, and attributes, special methods like `__str__` and `__repr__`, property/decorator use, and more.

## Requirements

- All scripts must be executable with exactly the same name as the task
- All modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- Code should use the PEP 8 style `(pycodestyle .)`

## Tasks

### [0. Simple rectangle]
Create a class `Rectangle` that defines a rectangle. For this first task, don't worry about attributes or methods; we'll add those throughout the project.

### [1. Real definition of a rectangle]
Now add attributes to your `Rectangle`. Include width and height, and make sure to validate them with getters and setters.

### [2. Area and Perimeter]
Add two new methods to your `Rectangle` class: `area` and `perimeter`. These should calculate and return the area and perimeter of the rectangle, respectively.

### [3. String representation]
Add the `__str__` special method to your class. This should return a string of '#' characters that represents the rectangle.

### [4. Eval is magic]
Add the `__repr__` special method to your class. This should return a string that can be used with `eval` to recreate an identical `Rectangle` object.

### [5. Delete it]
Add the `__del__` special method to your class. This should print a message whenever a `Rectangle` object is deleted.

## Author

[Nour Mellal]

[mellal.nour9@gmail.com]
