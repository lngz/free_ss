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
	url="http://www.ishadowsocks.net/"

	up=urllib2.urlopen(url)#打开目标页面，存入变量up

	lines =up.readlines()#从up中读入该HTML文件

	key1='服务器地址:'#设置关键字1
	key2="端口:"#设置关键字2
	key3="密码:"
	sites = []
	ports = []
	password = []
	for line in lines :
		m = re.match('.*服务器地址:(.*)</h4>', line)
		if m:
			# print m.group(1)
			sites.append(m.group(1))
		m = re.match('.*端口:(.*)</h4>', line)
		if m:
			# print m.group(1)
			ports.append(m.group(1))
		m = re.match('.*密码:(.*)</h4>', line)
		if m:
			# print m.group(1)
			password.append(m.group(1))
	i = int(sys.argv[1])
	print sites
	print ports
	print password

	return sites[i],ports[i], password[i]

sites, ports, password = get_free_ss()

i = int(sys.argv[1])
# print "shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password
# os.system("shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password)

if len(sys.argv) == 2:
	localbind = '1080'
else:
	localbind = sys.argv[2]


args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password ,"-l", localbind]
print args
child2 = subprocess.Popen(args)
# out = child2.communicate()
# print(out)


while 1:
	print "."
	time.sleep (1800)

	sites, ports, password1 = get_free_ss()
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


