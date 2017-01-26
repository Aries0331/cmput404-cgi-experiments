#!/usr/bin/env python

# ^ this thing is called the "shebang"

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])


print "content-type: text/html"

if username == "cd" and password == "ddd":
	print "Set-Cookie: loggedin=true"

print
print "<html><body>"
print "<h1>Hello World!</h1>"
print "Your magic tracking number is:"
print form.getvalue('magic_tracking_number')

print "<p>Your browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "Firefox"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome"
else:
  	print os.environ['HTTP_USER_AGENT']

# use post instead of get
print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

#print "<p>Username: " + form.getvalue('user')
#print "<p>Password: " + form.getvalue('password')

#check if usrname and password correct
print "<p>Username: " + str(username)
print "<p>Password: " + str(password)

if username == "cd" and password == "ddd":
	print "<p>Login successful!"



if "loggedin" in C:
	print "<p>Loggned in: " + str(C['loggedin'].value)
else:
	print "<p>No cookie"

#print json.dumps(dict(os.environ), indent=2, sort_keys=True)

