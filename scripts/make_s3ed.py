#!/bin/python
"""
make_s3ed.py: Connects to S3 bucket used for repositories to list all currently synced sites.
    The output is often piped to s3ed_sites.txt
How to call:
python make_s3ed.py  > s3ed_sites.txt
"""

import boto3

S3BUCKET = "ggis-repos"

client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket=S3BUCKET, Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix')[:-1])