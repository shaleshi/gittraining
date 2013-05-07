import os
import shutil
import sys
def main():
    print "hello"

def fread():
    a = sys.argv[1]
    fd = open('a.txt', 'r')
    str = fd.read(10);
    print str

    fw = open('a.txt', 'w')
    fw.write(a)
    fa = open('a.txt', 'a')
    fa.write("Hello")
    print fd.closed
    print fw.closed
    fd.close()
    fw.close()
    fa.close()

    shutil.copy('a.txt','b.txt')
if __name__ == '__main__':
    main()
    fread()

