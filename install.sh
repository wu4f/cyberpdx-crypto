#!/bin/bash
# Installs on Google Cloud Platform's Compute Engine for Ubuntu 20.04 LTS
# Make sure script is called with DNS name desired
if [ $# -ne 1 ]; then
    echo "Usage: sudo install.sh <DNS_Name>"
fi

# Name the service based on first part of DNS name
SITE=`echo $1 | sed -e 's/\..*//'`

# Install all required system packages
apt update
apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools virtualenv nginx python3-certbot-nginx

# Install all required python packages
virtualenv -p python3 env
source env/bin/activate
pip3 install --upgrade -r requirements.txt

# Set up systemd service for site
# Site will be run under the SUDO_USER
sed s+PROJECT_USER+$SUDO_USER+ etc/systemd.template | sed s+PROJECT_DIR+$PWD+ > /etc/systemd/system/$SITE.service

# Configure nginx for site
sed s+PROJECT_HOST+$1+ etc/nginx.template | sed s+PROJECT_DIR+$PWD+ > /etc/nginx/sites-available/$SITE
ln -s /etc/nginx/sites-available/$SITE /etc/nginx/sites-enabled

# Restart all services
systemctl start $SITE
systemctl enable $SITE
systemctl restart nginx

#certbot --nginx -d $1 -n -m wuchang@pdx.edu --agree-tos
