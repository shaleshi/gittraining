import os,sys
import subprocess
import pdb;pdb.set_trace()

def main():
    print "Hello"
    print "checking for the folder"
    #cwd = os.getcwd()
    #ldir = os.listdir('sada')
    subprocess.call('rm -fr sada', shell='true')
    a = os.mkdir('sada')
    print "directory is ",a

if __name__ == '__main__':
    main()
