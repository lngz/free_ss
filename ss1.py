#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
import re
import os
import subprocess
import time

def get_free_ss() :
	url="http://free.duj.me/"

	up=urllib2.urlopen(url)#打开目标页面，存入变量up

	lines =up.readlines()#从up中读入该HTML文件

	key1='服务器地址:'#设置关键字1
	key2="端口:"#设置关键字2
	key3="密码:"
	sites = []
	ports = []
	password = []
	method = []
	for line in lines :
		m = re.match('.*服务器地址:(.*?)</p>', line)
		if m:
			# print m.group(1)
			sites.append(m.group(1))
		m = re.match('.*端口:(.*?)</p>', line)
		if m:
			# print m.group(1)
			ports.append(m.group(1))
		m = re.match('.*密码:(.*?)</p>', line)
		if m:
			# print m.group(1)
			password.append(m.group(1))
		m = re.match('.*加密方式:(.*?)</p>', line)
		if m:
			# print m.group(1)
			method.append(m.group(1))

	
	return sites[0],ports[0], password[0],method[0]

sites, ports, password, method = get_free_ss()
print sites
print ports
print password
print method

# print "shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password + " -m " + method
# os.system("shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password + " -m " + method)
# child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password , "-m" , method]
print args
child2 = subprocess.Popen(args)
# out = child2.communicate()
# print(out)


while 1:
	print "."
	time.sleep (1800)

	sites, ports, password1, method = get_free_ss()
	print sites
	print ports
	print password1
	print method

	if password1 == password:
		continue
	else:
		child2.kill();
		password = password1
		args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , "-p" , ports , "-k" , password , "-m" , method]
		print args
		child2 = subprocess.Popen(args)



