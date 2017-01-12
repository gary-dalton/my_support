#!/bin/python
"""
update_wordpress: Runs updates on WordPress installations. The WordPress installation paths are passed
via argument pipe. After completion, it changes ownership back to www-data
How to call:
sudo find /var/www -name wp-config.php  | xargs sudo python update_wordpress.py
"""

import sys
import subprocess

thefiles = sys.argv[1:]

for filepath in thefiles:
    print("----------")
    print("Updates available on " + filepath[:-13])
    subprocess.call('wp plugin update --allow-root --all --path=' + filepath[:-13], shell=True)
    subprocess.call('wp theme update --allow-root --all --path=' + filepath[:-13], shell=True)
    subprocess.call('wp core update --allow-root --path=' + filepath[:-13], shell=True)
    subprocess.call('wp core update-db --allow-root --path=' + filepath[:-13], shell=True)
    subprocess.call('chown -R www-data:www-data ' + filepath[:-13], shell=True)
    print("----------")
