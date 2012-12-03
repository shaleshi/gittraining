import os
import sys
import subprocess

def installPython():
    """Installing the python26"""
    print "******************python path *********************"
    py_to_path = os.path.join("usr", "bin", "python")
    if not os.path.exists(py_to_path):
        print "***************Installing the python************"
        subprocess.call('./installpython.sh -s',shell=True)
def runBootstrap():
    """Bootstraping the buildout"""
    py_path = sys.executable
    print py_path
    print "***********Bootstraping th buildout *****************"
    subprocess.call("%s bootstrap.py"%py_path, shell = True)

def runBuildout():
    """Running the buildout"""
    print "*************Running the buildout********************"
    subprocess.call("bin/buildout -c jenkins.cfg",shell = True)

def startJenkins():
    """Starting the jenkins server"""
    print "***************Starting the jenkins server************"
    subprocess.call('bin/run_jenkins.sh', shell = True)

def main():
    installPython()
    runBootstrap()
    runBuildout()
    startJenkins()


if __name__ == '__main__':
    main()
