#!/usr/bin/env python

'''
Application 3 of the Udemy Python Course. It will block deemed "distracting" websites
for a given time. It will automatically add redirect lines to the system host file
at a given time of day.
'''

#HOSTS LOCATION C:\Windows\System32\drivers\etc
#MAC/LINUX /etc/hosts

import time
from datetime import datetime as dt

path = r"C:\Windows\System32\drivers\etc\hosts"
reDirect = "127.0.0.1"
blockedSites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

def blockSites():
    '''
    The main function.
    '''
    while True:

        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now()\
            < dt(dt.now().year, dt.now().month, dt.now().day, 16):

            print("Access Denied: " + str(blockedSites))
            with open(path, 'r+') as file:
                content = file.read()
                for website in blockedSites:
                    if website in content:
                        pass
                    else:
                        file.write(reDirect + " " + website + "\n")

        else:

            print("Access Granted: " + str(blockedSites))
            with open(path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in blockedSites):
                        file.write(line)
                file.truncate()

        time.sleep(5)

blockSites()
