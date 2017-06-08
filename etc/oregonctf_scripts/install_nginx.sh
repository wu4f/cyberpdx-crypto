# Installs on Google Cloud Platform's Compute Engine for Ubuntu 16.04 LTS
# Modify servername in nginx/sites-available/metactf to match your hostname
# then do the restart

apt-get update
apt-get upgrade -y
apt-get install -y build-essential python3-pip nginx uwsgi uwsgi-plugin-python3 zsh openssl bc
pip3 install virtualenv
usermod -g www-data $SUDO_USER
cat /etc/login.defs | sed -e '/^UMASK/ s/022/002/' > /tmp/login.defs
mv /tmp/login.defs /etc/login.defs
chown -R $SUDO_USER:www-data /var/www/html
chmod -R g+rwX /var/www/html
