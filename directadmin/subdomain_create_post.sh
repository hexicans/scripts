#!/bin/sh
#
# Author: Phantium
#
# Move DirectAdmin subdomain folder to correct (/home/$username/domains/$subdomain) location
# This is simply more neat than putting everything under the public_html of the domain root
#
# For this you also need to copy both virtual_host2_secure_sub.conf and virtual_host2_sub.conf to
# /usr/local/directadmin/data/templates/custom and modify them to your wishes.
#
# Generally changing to DOCROOT and REALDOCROOT to e.g. `HOME`/domains/`SUB`.`DOMAIN`/public_html| 
# and omitting |SUB| from all paths will do.
#
# FYI: Variables $username, $domain and $subdomain are given directly by DirectAdmin to the script.
##

OLD_FOLDER=/home/$username/domains/$domain/public_html/$subdomain
NEW_FOLDER=/home/$username/domains/$subdomain.$domain/public_html

# SSL, optional (uncomment if you use subdomains with SSL and care about the default index.html, I do not.)
#OLD_FOLDER_SSL=/home/$username/domains/$domain/private_html/$subdomain
#NEW_FOLDER_SSL=/home/$username/domains/$subdomain.$domain/private_html

#mkdir -p -m 0751 ${NEW_FOLDER_SSL}
#chown ${username}:${username} ${NEW_FOLDER_SSL}
#cp ${OLD_FOLDER_SSL}/index.html ${NEW_FOLDER_SSL}/index.html

mkdir -p -m 0751 ${NEW_FOLDER}
chown ${username}:${username} ${NEW_FOLDER}
cp ${OLD_FOLDER}/index.html ${NEW_FOLDER}/index.html

# Delete old subdomain folder with all of its contents, off by default.
#rm -rf ${OLD_FOLDER}

# Optionally add symlink in public_html/$subdomain to the subdomain folder contents.
# Will basically mimic old behavior, without the messy structure.
# !!! Before you do this, make sure the old subdomain folder deletion is turned ON !!!
#ln -s ${NEW_FOLDER} ${OLD_FOLDER}

# DirectAdmin wishes to receive this.
exit 0;
