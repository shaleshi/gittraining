#webbrowser = Convenient Web-browser controller
import webbrowser
url = 'http://www.python.org/'
webbrowser.open_new_tab(url + 'doc/')
webbrowser.open_new(url)

#cgi  Common Gateway Interface support
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"
##################################################
#urllib  Open arbitrary resources by URL
import urllib2 #extensible library for opening URLs
import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
print f.read()
f = urllib2.urlopen('http://www.python.org/')
print f.read(100)

import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason

#ftplib  FTP protocol client
import ftplib
#poplib  POP3 protocol client
import poplib
#imaplib  IMAP4 protocol client
import imaplib
#nntplib  NNTP protocol client, The Network News Transfer Protocol (NNTP)
import nntplib
#smtplib  SMTP protocol client
import smtplib
#sender = mailid
#receivers = mailid
#message = type message
#smtpObj = smtplib.SMTP('localhost')
#smtpObj.sendmail(sender, receivers, message)
#smtpd  SMTP Server
import smtpd
#telnetlib  Telnet client
import telnetlib
#uuid  UUID objects according to RFC 4122
import uuid
#urlparse  Parse URLs into components
import urlparse
from urlparse import urlparse
obj = urlparse('http://www.google.com')
print obj
import urlparse
url = 'HTTP://www.Python.org/doc/#'
r1 = urlparse.urlsplit(url)
r1.geturl()
#SocketServer  A framework for network servers
import SocketServer
#BaseHTTPServer — Basic HTTP server
import BaseHTTPServer
#SimpleHTTPServer — Simple HTTP request handler
import SimpleHTTPServer
#CGIHTTPServer  CGI-capable HTTP request handler
import CGIHTTPServer
#cookielib  Cookie handling for HTTP clients
import cookielib
#Cookie  HTTP state management
import Cookie
#xmlrpclib  XML RPC client access
import xmlrpclib
#SimpleXMLRPCServer  Basic XML-RPC server
import SimpleXMLRPCServer
#DocXMLRPCServer  Self-documenting XML-RPC server
import DocXMLRPCServer


###################################################
import wsgiref.util #import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
        for key, value in environ.iteritems()]
    return ret

httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()
