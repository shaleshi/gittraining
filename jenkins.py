import os
import sys
import subprocess

def installPython():
    """Installing the python26"""
    py_to_path = os.path.join("usr", "bin", "python")
    if not os.path.exists(py_to_path):
        subprocess.call('./installpy.sh -s',shell=True)
def runBootstrap():
    py_path = sys.executable
    print py_path
    subprocess.call("%s bootstrap.py"%py_path, shell = True)

def runBuildout():
    subprocess.call("bin/buildout -c jenkins.cfg",shell = True)

def startJenkins():
    wd = os.getcwd()
    print wd
    os.system('source bin/run_jenkins.sh')

def main():
    installPython()
    runBootstrap()
    runBuildout()
    startJenkins()


if __name__ == '__main__':
    main()
