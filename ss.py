#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
import subprocess
import time

def get_free_ss() :
	url="http://abc.ishadow.online/"

	up=urllib2.urlopen(url)#打开目标页面，存入变量up

	lines =up.readlines()#从up中读入该HTML文件


	sites = []
	ports = []
	password = []
	method = []
	for line in lines :

		
		m = re.match('.*<h4>IP Address:<span id=".*?">(.*?)</span>.*', line)
		if m:
			print line
			print m.group(1)
			sites.append(m.group(1))
		m = re.match('.*<h4>Port：(\d+)</h4>', line)
		if m:
			# print m.group(1)
			ports.append(m.group(1))
		m = re.match('.*<h4>Password:<span id=".*?">(.*?)</span>', line)
		if m:
			# print m.group(1)
			password.append(m.group(1))
		m = re.match('.*<h4>Method:(.*)</h4>', line)
		if m:
			# print m.group(1)
			method.append(m.group(1))
	i = int(sys.argv[1])
	print sites
	print ports
	print password

	return sites[i],ports[i], password[i],method[i]

sites, ports, password ,method= get_free_ss()

i = int(sys.argv[1])
# print "shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password
# os.system("shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password)

if len(sys.argv) == 2:
	localbind = '1080'
else:
	localbind = sys.argv[2]


args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , 
                                            "-p" , ports , 
                                            "-k" , password ,
                                            "-m" , method,
                                            "-l", localbind]
print args
child2 = subprocess.Popen(args)
# out = child2.communicate()
# print(out)


while 1:
	print "."
	time.sleep (1800)

	sites, ports, password1 ,method= get_free_ss()
	print sites
	print ports
	print password1
	

	if password1 == password:
		continue
	else:
		child2.kill();
		password = password1
		args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password , "-l", localbind]
		print args
		child2 = subprocess.Popen(args)


