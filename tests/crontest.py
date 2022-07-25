#!/usr/bin/env python3
"""crontest.py
test script to stop cron jobs and switch features.
"""
from crontab import CronTab
import os

# prompt to check if stable/beta is running. it answers.
# option to enable/re-enable Stable from directory.
# option to disable stable

# TEST CODE BELOW

hostname = "www.asukasoftware.com/api/Online"
response = os.system("ping -c 1 " + hostname)


cron = CronTab(user='ubuntu')

job = cron.new(command='cd /home/ubuntu/stable/Banjo_api && /usr/bin/bash /home/ubuntu/stable/Banjo_api/startup.sh', comment='Stable API Running')

search = cron.find_comment('Stable API')

# STEP 1 check if stable is running via. cron? bash? - in progress

if (response == 0):
    print("Stable API is running!")
    # STEP 2 if step 1 shows it is online. Ask to kill it & remove from file.
    val = input("Disable Stable API?: Y/y")
    if (val == "Y" or val == "y"):
        cron.remove(job)
        print ("Job deleted")
    else:
        exit()
else:
    # step 2.1 if step 1 show it is offline. Ask to run it and add to file.
    print("Stable API is not running")
    val = input("Enable Stable API?: Y/y")
    if (val == "Y" or val == "y"):
        job.minute.every(1) # check later for proper scheduling
        cron.write()
        print ("Job created")
    else:
        exit()
