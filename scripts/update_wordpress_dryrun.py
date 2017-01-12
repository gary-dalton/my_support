#!/bin/python
"""
update_wordpress_dryrun.py: Dry runs updates on WordPress installations. The WordPress installation paths are passed
via argument pipe.
How to call:
sudo find /var/www -name wp-config.php  | xargs sudo python update_wordpress_dryrun.py
"""

import sys
import subprocess

thefiles = sys.argv[1:]

for filepath in thefiles:
    print("----------")
    print("Updates available on " + filepath[:-13])
    subprocess.call('wp plugin update --allow-root --all --dry-run --path=' + filepath[:-13], shell=True)
    subprocess.call('wp theme update --allow-root --all --dry-run --path=' + filepath[:-13], shell=True)
    subprocess.call('wp core check-update --allow-root --path=' + filepath[:-13], shell=True)
    print("----------")
