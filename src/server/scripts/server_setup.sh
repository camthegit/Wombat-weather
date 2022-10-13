#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv

# Stop the hackers
sudo apt install fail2ban -y

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable


apt install acl -y
useradd -M apiuser
usermod -L apiuser


# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/weather_api
mkdir /apps/logs/weather_api/app_log
# chmod 777 /apps/logs/weather_api
setfacl -m u:apiuser:rwx /apps/logs/weather_api
# cd /apps

# Create a virtual env for the app.
cd /apps
python3 -m venv venv
source /apps/venv/bin/activate

# add source command to ~/.zshrc

pip install --upgrade pip setuptools wheel
pip install --upgrade httpie glances
pip install --upgrade gunicorn uvloop httptools

# clone the repo:
cd /apps
# git clone https://github.com/talkpython/modern-apis-with-fastapi app_repo
git clone https://github.com/camthegit/temp-obs-api.git huey

# Setup the web app:
cd /apps/huey
pip install -r requirements.txt

# can run with python main.py and check output with http localhost:8000

## TEST the daemon start command first
# Copy and enable the daemon
cp /apps/obs/src/server/units/weather.service /etc/systemd/system/

systemctl start weather
systemctl status weather
systemctl enable weather

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/obs/src/server/nginx/weather.nginx /etc/nginx/sites-enabled/
update-rc.d nginx enable
service nginx restart


# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

## DEPRECATED
# add-apt-repository ppa:certbot/certbot
# apt install python3-certbot-nginx
# certbot --nginx -d weatherapi.talkpython.com

## NO - from https://certbot.eff.org:
sudo snap install core; sudo snap refresh core
# Install
snap install --classic certbot
# Test the link command (?? actual intent here)
ln -s /snap/bin/certbot /usr/bin/certbot
# Install cert and configure nginx
certbot --nginx
# test automatic renewal
certbot renew --dry-run

