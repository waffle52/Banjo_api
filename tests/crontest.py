#!/usr/bin/env python3
"""crontest.py
test script to stop cron jobs and switch features.
"""
from crontab import CronTab

# prompt to check if stable/beta is running. it answers.
# option to enable/re-enable Stable from directory.
# option to disable stable

# STEP 1 check if stable is running via. cron? bash?


# STEP 2 if step 1 shows it is online. Ask to kill it & remove from file? 

# STEP 2.1 if step 1 show it is offline. Ask to enable it by adding it to cron file. 


# TEST CODE BELOW

cron = CronTab(user='ubuntu')

job = cron.new(command='cd /home/ubuntu/stable/Banjo_api && /usr/bin/bash /home/ubuntu/stable/Banjo_api/startup.sh', comment='Stable API Running')

search = cron.find_comment('Stable API')

for item in search:
    print (item)

# second test with adding job
job = cron.new(command='cd /home/ubuntu/stable/Banjo_api && /usr/bin/bash /home/ubuntu/stable/Banjo_api/startup.sh', comment='Stable API Running')
job.minute.every(1)

cron.write()

search = cron.find_comment('Stable API')

for item in search:
    print (item)

cron.remove(job)
print ("Job removed")
