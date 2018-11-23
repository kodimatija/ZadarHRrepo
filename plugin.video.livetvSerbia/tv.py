#!/usr/bin/python
# coding: UTF-8
# support stevegtdbz@gmail.com

'''
	Description: tv-streaming
	Version: v1 (last update 25/9/17)
'''

import urllib2, os, time, pickle, json, sys, re

# Functions
def fileExist(f): return True if os.path.isfile(f) else False
def exit(msg):
	print "red"
	sys.exit(1)

# Variables 
MAIN_LINK = "https://tv.iskon.hr/ezjscore/call/IskonTvPlayer::getStream::id::"
USER_AGENT = "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
COOKIE = "paeb0flvr5aj11i7eeh4vr61l5; path=\"/\"; domain=tv.iskon.hr; path_spec; expires=\"0\"; version=0; tvplayer_kv=1.E.1.ukxUoB7Ks9vA3xIFwLO6bdSJ6x0OahsNhMR_0luk83Ikj1zhMfoYEuk0z0acbkJl_wvSJMKh1gB5I1EvOBXYOQRycor3sw21JY9FkcHkKX37ucsSLccFouHqMVDpNtoI6ybj61lekILCt2tf_DqDqBSlgea524NZIiEeCB5RWF2r1kRZwXsydoMSMwtadR2zVoeZOT4jNu_j1YApsbzEkipSt2xpcjryT00sexq8PKQKHi70pnnsuIn1QOQGE4Puo3rczT6cxEAIKvwfkV9ztkyrFd_2ihLkMYmCOVXMLNjXISx3Vqk_7T6RoGYm6XgUk4y4OzQlidulY7LhYREt3dW6xA5Vs7KOG2S6_ts7Lj3EZ9pwJca9dA5UULo4qkAeBoPDz-NiiFpBmaDCAtD7DyKMhBgMlrKitaj5t7CmkMLZwSPnjQ-1_CWZVam0E1kmzHgXgjnFT2XjoZ6kgaVUOA.YNlk9dR-OtMxi1mYMZ9Y8XK9lHqNuknkm1a9V5mr0CM; path=\"/\"; domain=tv.iskon.hr; path_spec; expires=\"1510453949.839\"; version=0"

HEADER = "#EXTM3U\n#EXTVLCOPT--http-reconnect=true\n"

OUTPUT_FILE_1 = "python_IskonTV_by_losmij.m3u"
OUTPUT_FILE_2 = "python_IskonTV_by_losmij-rtmp.m3u"
INPUT = "id.txt"

# Init
if not fileExist(INPUT): exit("["+INPUT+"] File not found")
ids = []
with open(INPUT) as f:
	for line in f:
		ids.append(line.strip())
        f.close()

# Requests
reqData = []
for idValue in ids:
	print "REQUEST ID -> "+(str)(idValue)
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', USER_AGENT)]
	opener.addheaders = [('Cookie', COOKIE)]
	data = opener.open(MAIN_LINK+idValue).read()
	reqData.append(data)

# Write Files
print "WRITE FILE -> "+OUTPUT_FILE_1
f = open(OUTPUT_FILE_1, 'w')
f.write(HEADER)
for req in reqData:
	try:
		fields = req.split(',')
		f.write("#EXTVLCOPT:http-user-agent=losmij\n#EXTINF:-1,"+fields[5]+"\n"+fields[2]+"/"+fields[4]+"?username="+fields[0]+"&s="+fields[1]+"&stream_count="+fields[3]+"\n")
	except Exception, e:
		print (str)(e)
f.close()

print "WRITE FILE -> "+OUTPUT_FILE_2
f = open(OUTPUT_FILE_2, 'w')
f.write(HEADER)
for req in reqData:
	try:
		fields = req.split(',')
		first = fields[2][:fields[2].rfind('/')+1].replace("http", "rtmp").replace("80","1935")
		last = fields[2][fields[2].rfind('/')+1:]
		typeOf = last[last.find(':')+1:last.rfind('w')] 
		path = first+typeOf
		f.write("#EXTVLCOPT:http-user-agent=losmij\n#EXTINF:-1,"+fields[5]+"\n"+path+"_b3.stream?username="+fields[0]+"&s="+fields[1]+"&stream_count="+fields[3]+"\n")
	except Exception, e:
		print (str)(e)
f.close()


