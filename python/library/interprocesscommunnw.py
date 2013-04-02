#subprocess  Subprocess management
#The subprocess module allows you to spawn new processes, connect to their
#input/output/error pipes, and obtain their return codes.
import subprocess
print dir(subprocess)
subprocess.Popen(["ls", "-l"])
print dir(subprocess.Popen)#Has some more options li kill,wait,terminate
#socket Low-level networking interface
import socket #IPv4
#Secure Sockets Layer SSL wrapper for socket objects
import ssl
#signal Set handlers for asynchronous events
import signal
#popen2.popen2(cmd[, bufsize[, mode]])
#Executes cmd as a sub-process. Returns the file objects (child_stdout, child_stdi)
#asyncore Asynchronous socket handler
import asyncore
#asynchat  Asynchronous socket command/response handler
import asynchat
