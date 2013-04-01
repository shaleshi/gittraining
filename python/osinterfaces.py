#If you just want to read or write a file see open()
#if you want to manipulate paths, see the os.path module
#for high-level file and directory handling see the shutil module.
#What are all the possible command operation we perform in linux/windows we can perform using the os in python
import os
print dir(os)
print dir(os.path)
print os.listdir(os.getcwd())
#os.popen(...)#run the child process
#os.sysitem('./installpython.sh -s')#run like linux shell commands
print os.curdir
print os.pardir
import io #with open
import time
import datetime
#optparse  More powerful command line option parser
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
