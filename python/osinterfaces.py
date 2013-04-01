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
def main():
	usage 	= "usage:%prog [options] arg1 arg2"
	parser = OptionParser(usage=usage)
	parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
	parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

	(options, args) = parser.parse_args()
if __name__ == '__main__':
	main()

#parser.add_option(opt_str, ...,attr=value, ...) #basic syntax
#Once all of your options are defined, instruct optparse to parse your programs command line
#(options, args) = parser.parse_args()
#parse_args takes two arguments
#options, an object containing values for all of your options e.g. if "--file" takes a single string argument
#args, the list of positional arguments leftover after parsing options
#The most common option action is store, which tells optparse to take the next argument (or the remainder of the current argument),
# ensure that it is of the correct type, and store it to your chosen destination.
#getopt   Parser for command line options
#logging   Logging facility for Python
import logging
LOG_FILENAME = 'log_file.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug("This message should go into the log file")
#getpass   Portable password input
#curses   Terminal handling for character-cell displays
#curses   ascii Utilities for ASCII characters
#curses   panel A panel stack extension for curses
#errno    Standard errno system symbols
