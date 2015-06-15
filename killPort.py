import os
import sys
import subprocess


port = ""

if len(sys.argv) < 2:
	print "Proper Usage: killport.py <port>"
	sys.exit(1)

for arg in sys.argv:
	port = arg	

command = "lsof -i tcp:%s | awk 'NR!=1 {print$2}'" % port
kill_command = command + " | xargs kill -9"
#print command

stdout = subprocess.check_output(command, shell=True)

if len(stdout) < 1:
	print "No processes using that port"
	sys.exit(0)
else:
	print "List of all pids using Port: %s" % port
	print stdout


answer = raw_input('Would you like to slaughter these processes? (yes/no) ')

if answer == "yes":
	print "KILL THEM ALL!!!!!"
	print kill_command
	stdout = subprocess.check_output(kill_command, shell=True)
	print stdout
else:
	print "wuss..."

