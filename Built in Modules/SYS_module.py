import sys
#The sys module is a built-in Python module that provides access to variables and functions related to the Python interpreter.

import sys

# Python version
print("Python Version:")   # sys.version → Displays Python version.
print(sys.version)

# Operating System
print("\nPlatform:")  # sys.platform → Displays the operating system.
print(sys.platform)

# Command-line arguments
print("\nCommand-Line Arguments:") # sys.argv → Displays command-line arguments.
print(sys.argv)

# Python module search path
print("\nModule Search Path:")  # sys.path → Displays the module search path.
print(sys.path)

# Maximum integer size
print("\nMaximum Integer Size:") # sys.maxsize → Displays the maximum integer size.
print(sys.maxsize)

# Size of an object
num = 100
name = "Python"
li = [10, 20, 30]

print("\nSize of Integer:", sys.getsizeof(num), "bytes")  # sys.getsizeof() → Returns the size of an object in bytes.
print("Size of String:", sys.getsizeof(name), "bytes")      
print("Size of List:", sys.getsizeof(li), "bytes")

# Exit the program
print("\nProgram is about to exit...")  # sys.exit() → Terminates the program.
sys.exit()

print("This line will not execute.")
