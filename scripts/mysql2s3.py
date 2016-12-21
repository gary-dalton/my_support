#!/bin/python
"""
mysql2s3.py: Pulls credentials from the files passed via command line.
Then it calls the mysqldump command to backup databases. Finally,
it syncs the backed up databases to an AWS S3 bucket
How to call:
sudo find /var/www -name wp-config.php  | xargs sudo python mysql2s3.py
"""

import sys
import re
import datetime
import subprocess

# Some variables that you may choose to change.
SITEDIR = "/var/www/"
DUMPDIR = "/var/local/dbdumps/"
S3BUCKET = "s3://ggis-repos/"

# Compile our regexes
DB_NAME = re.compile("DB_NAME.*'(.*)'")
DB_USER = re.compile("DB_USER.*'(.*)'")
DB_PASSWORD = re.compile("DB_PASSWORD.*'(.*)'")

# Build date string
todaystring = datetime.date.today().isoformat()

thefiles = sys.argv[1:]

for filename in thefiles:
    with open(filename) as f:
        text = f.read()
    f.close()
    name_match = DB_NAME.findall(text)
    user_match = DB_USER.findall(text)
    password_match = DB_PASSWORD.findall(text)
    # print(name_match, user_match, password_match)
    result_file = DUMPDIR + name_match[0] + todaystring + '.sql'
    arg1 = '--user=' + user_match[0]
    arg2 = '--password=' + password_match[0]
    arg3 = '--opt'
    arg4 = '--result-file=' + result_file
    subprocess.call(['mysqldump', arg1, arg2, arg3, arg4, name_match[0]])
    subprocess.call(['gzip', result_file])

subprocess.call(['aws', 's3', 'sync', DUMPDIR, S3BUCKET, '--delete'])
