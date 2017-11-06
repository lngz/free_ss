#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
import subprocess
import time
import random
import base64

def get_free_ss() :
    url="https://ss.ishadowx.net/"

    up=urllib2.urlopen(url)#打开目标页面，存入变量up

    lines =up.readlines()#从up中读入该HTML文件


    sites = []
    ports = []
    password = []
    method = []
    qr = []
    for line in lines :

        
        m = re.match('.*<h4>IP Address:<span id=".*?">(.*?)</span>.*', line)
        if m:
            print line
            print m.group(1)
            sites.append(m.group(1))
        m = re.match('.*<h4>Port:<span id=".*?">(\d+)', line)
        if m:
            # print m.group(1)
            ports.append(m.group(1))
        m = re.match('.*<h4>Password:<span id=".*?">(.*?)', line)
        if m:
            # print m.group(1)
            password.append(m.group(1))
        m = re.match('.*<h4>Method:(.*)</h4>', line)
        if m:
            # print m.group(1)
            method.append(m.group(1))
        m = re.match('.*<h4><a href="(img/qr/.*\.png)"(.*)</h4>', line)
        if m:
            # print m.group(1)
            qr.append(m.group(1))
    
    print sites
    print ports
    print password
    print method
    print qr
    
    i = random.randint(0,len(sites)-1)
    if not password[i] == '':
        return sites[i],ports[i], password[i],method[i]
    else:
    	try:
    		qr_code = subprocess.check_output(['zbarimg', '-q', url+qr[i]])
    	except Exception as e:
    		return sites[i],ports[i], password[i],method[i]
        
        # print qr_code
        return get_free_qr(qr_code)

def get_free_qr(qr) :
	#QR-Code:ss://cmM0LW1kNToxMTgwOTE1MkAxNTMuOTIuNDMuNjQ6NDQzCg==

	SS = qr
	ss = base64.b64decode(SS.split('/')[2])
	method = ss.split(':')[0]
	ports = ss.split(':')[2].strip()
	password = ss.split(':')[1].split('@')[0]
	sites = ss.split(':')[1].split('@')[1]

	print sites
	print ports
	print password


	
	return sites,ports, password,method

# sites, ports, password, method = get_free_qr()
sites, ports, password ,method= get_free_ss()


# print "shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password
# os.system("shadowsocks/shadowsocks/local.py -s " + sites + " -p " + ports + " -k " + password)


localbind = '1080'


args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , 
                                            "-p" , ports , 
                                            "-k" , password ,
                                            "-m" , method,"-v",
                                            "-l", localbind]
print args
child2 = subprocess.Popen(args)
# out = child2.communicate()
# print(out)


while 1:
    print "."
 
    time.sleep (2)

    ret = os.system('curl --connect-timeout 10 --socks5-host 127.0.0.1:1080 www.google.com')

    if ret == 0:
        time.sleep (1800)
        continue
    else:
        child2.kill();
        sites, ports, password1 ,method= get_free_ss()
        print sites
        print ports
        print password1
        password = password1
        args = ["shadowsocks/shadowsocks/local.py", "-s" , sites , 
                                            "-p" , ports , 
                                            "-k" , password ,
                                            "-m" , method,"-v",
                                            "-l", localbind]

        print args
        child2 = subprocess.Popen(args)


