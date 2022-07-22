#!/usr/bin/env python3
"""crontest.py
test script to stop cron jobs and switch features.
"""
from crontab import CronTab

# prompt to check if stable/beta is running. it answers.
# option to enable/re-enable Stable from directory.
# option to disable stable


cron = CronTab(user='root')

for job in cron:
    print(job)
