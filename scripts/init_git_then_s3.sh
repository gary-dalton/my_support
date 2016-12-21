#!/bin/bash
#
# This script must be run as sudo.
# This script expects site names input from a file.
# Call this script thusly:
# sudo ./init_git_then_s3.sh $(cat todo_sites.txt)

# Some variables that you may choose to change.
SITEDIR="/var/www/"
REPOSDIR="/var/local/repos/"
S3BUCKET="ggis-repos"

SITES="$@"
for f in $SITES
do
    cd $SITEDIR$f
    git init $SITEDIR$f
    git add --all
    git commit -m "Initial commit of site"
    git clone $SITEDIR$f $REPOSDIR$f
    aws s3 sync $REPOSDIR$f s3://$S3BUCKET/$f --delete

done