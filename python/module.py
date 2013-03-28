"""
As your program gets longer, you may want to split it into several files for easier maintenance
A module is a file containing Python definitions and statements
definitions from a module can be imported into other modules or into the main module

"""
def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
"""
import module
module.fib(10)
module.__name__ #returns the program name
from module import *
"""

"""Executing the modules as scripts"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
"""Module search in the sys.path"""
"""As an important speed-up of the start-up time for short programs that use a lot of standard modules,
if a file called spam.pyc exists in the directory where spam.py is found,
this is assumed to contain an already-“byte-compiled” version of the module spam.
"""
""".pyc or .pyo speed up the execution of program instead of the .py"""
"""Suppose you want to design a collection of modules (a “package”).
__init__.py               Initialize the sound package
"""

