import math
print '{0} and {1}'.format('spam', 'eggs')
print 'The value of PI is approximately %5.3f' % math.pi
#a = open('file', 'mode') #mode rwa,r+,w+
#f.write('This is a test\n')
"""It is good practice to use the with keyword when dealing with file objects.
This has the advantage that the file is properly closed after its suite finishes,
even if an exception is raised on the way. It is also much shorter than writing equivalent try-finally blocks:

>>> with open('/tmp/workfile', 'r') as f:
...     read_data = f.read()

pickle This is an amazing module that can take almost any Python object (even some forms of Python code!),
and convert it to a string representation; this process is called pickling.
Reconstructing the object from the string representation is called unpickling

Execption
while True:
...     try:
...         x = int(raw_input("Please enter a number: "))
...         break
...     except ValueError:
...         print "Oops!  That was no valid number.  Try again..."

try:
...     raise KeyboardInterrupt
... finally:
...     print 'Goodbye, world!'
...
Goodbye, world!
A finally clause is always executed before leaving the try statement,
whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled
by an except clause (or it has occurred in a except or else clause
it is re-raised after the finally clause has been executed
The finally clause is also executed on the way out when any other clause of the try
"""
