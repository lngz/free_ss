#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
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


print sites
print ports
print password
i = int(sys.argv[1])
print "shadowsocks/shadowsocks/local.py -s " + sites[i] + " -p " + ports[i] + " -k " + password[i]
os.system("shadowsocks/shadowsocks/local.py -s " + sites[i] + " -p " + ports[i] + " -k " + password[i])
