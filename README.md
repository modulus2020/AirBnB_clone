# AirBnB clone - The console

# Table of contents
* Introduction
* Installation
* Model
* Testing
* Author

# Introduction
This is team project to build a clone of AirBnB

The console is a command interpreter to manage objects abstraction between objects and how they are stored

The console will perform thr following tasks:
* create a new object
* retrieve an object from a file
* do operations on objects
* update attributes of an object
* destroy an object

**Storage**
All the classes are handled by the **Storage** engine in the **FileStorage** Class

# Installation
**Execution**
Interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

Non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

# Model
This contains the class **BaseModel** that defines all common attributes/methods for other classes

# Testing
All the test are defined in the **tests** folder

**Documentation**
* Modules:
python3 -c 'print(__import__("my_module").__doc__)'

* Classes:
python3 -c 'print(__import__("my_module").MyClass.__doc__)'

* Functions:
python3 -c 'print(__import__("my_module").my_function.__doc__)'

and

python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

**Python Unit Tests**
* Unittest module
* File extension
* Files and folder start by **test_**
* File organisation: For models/base.py, unit tests in: tests/test_models/test_base.py
* Execution command: python3 -m unittest discover tests
* or: python3 -m unittest tests/test_models/test_base.py

**run test in interactive mode**
echo "python3 -m unittest discover tests" | bash

**run test in interactive mode**
python3 -m unittest discover tests

# Authors
* Odjuvwederhie Blessing
* Jackson Joshua
