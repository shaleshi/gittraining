import os
import subprocess
#def argpars():
#	"""argparse  module automatically generates the help 
#	   and command line usage ehn user gives the program
#	   invalid arguments
#	"""
#    print "Hello"

def git_clone(repo):
    print "Hello"
    subprocess.call("git clone %s git"%options.git_repo, shell=True)     
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-g", "--gitrepo", dest="git_repo",help="Please spefify the git repo", metavar="")
    parser.add_option("-q", "--quiet",action="store_false", dest="verbose", default=True,help="don't print status messages to stdout")

(options, args) = parser.parse_args()
#options object contains all of your options -g,--gitrepo will store
#args list of positional arguments left over after parsing arguments
repo = git_clone(options.git_repo)

    

