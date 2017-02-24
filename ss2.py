#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
import subprocess
import time
import base64

def get_free_ss() :
	#QR-Code:ss://cmM0LW1kNToxMTgwOTE1MkAxNTMuOTIuNDMuNjQ6NDQzCg==

	SS = sys.argv[1]
	ss = base64.b64decode(SS.split('/')[2])
	method = ss.split(':')[0]
	ports = ss.split(':')[2].strip()
	password = ss.split(':')[1].split('@')[0]
	sites = ss.split(':')[1].split('@')[1]

	print sites
	print ports
	print password


	
	return sites,ports, password,method

sites, ports, password, method = get_free_ss()
print sites
print ports
print password
print method

if len(sys.argv) == 2:
	localbind = '1080'
else:
	localbind = sys.argv[2]

# print "shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password + " -m " + method
# os.system("shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password + " -m " + method)
# child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password , "-m" , method, "-l", localbind]
print args
child2 = subprocess.Popen(args)
out = child2.communicate()
print(out)


# while 1:
# 	print "."
# 	time.sleep (300)

# 	sites, ports, password1, method = get_free_ss()
# 	print sites
# 	print ports
# 	print password1
# 	print method

# 	if password1 == password:
# 		continue
# 	else:
# 		child2.kill();
# 		password = password1
# 		args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password , "-m" , method]
# 		print args
# 		child2 = subprocess.Popen(args)




