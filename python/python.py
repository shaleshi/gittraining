#comment
>>> primary prompt
... secondary prompt
a = 10
b = 1
a*b
Complex : (3+1j)*3
A raw string literal is simply a string literal that does not recognize C++ escape sequences.
word = 'Hello ' + 'Welcome'
word[4]
word[:2]
'x' + word[1:]
word[:2] + word[2:] = word
word[-1]     # The last character
word[-0]     # (since -0 equals 0)
len(word)
How slice works
==============
+---+---+---+---+---+
| H | e | l | p | A |
+---+---+---+---+---+
0  1  2   3   4   5
-5  -4  -3  -2  -1

List
        +0      +1   +2     +3
a = ['spam', 'eggs', 100, 1234]
        -4      -3    -2    -1

Nesting of list
q = [2, 3]
p = [1, q, 4]
we can use Python for more complicated tasks.
any non-zero integer value is true; zero is false.
indentation is Python’s way of grouping statements.
if #condition check
for # looping
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

break and continue Statements, and else Clauses on Loop
The return statement returns with a value from a function.
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

PEP:Index of Python Enhancement Proposals
Set
===
A set is an unordered collection with no duplicate elements
tel = {'jack': 4098, 'sape': 4139}
Looping the dict
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.iteritems():
        print k, v
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
