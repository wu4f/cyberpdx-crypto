# Installs on Google Cloud Platform's Compute Engine for Ubuntu 16.04 LTS
# Takes the site name as an argument
cd /var/www/html
chown -R $SUDO_USER .
git clone https://wuchangfeng@bitbucket.org/wuchangfeng/cyberpdx_crypto_2017.git
cd /var/www/html/
mv cyberpdx_crypto_2017 cyberpdx
cd cyberpdx
mv etc/nginx/sites-available/cyberpdx /etc/nginx/sites-available/cyberpdx
mv etc/nginx/sites-enabled/cyberpdx /etc/nginx/sites-enabled/cyberpdx
cd /var/www/html/cyberpdx
mv etc/uwsgi/apps-available/cyberpdx.ini /etc/uwsgi/apps-available/cyberpdx.ini
mv etc/uwsgi/apps-enabled/cyberpdx.ini /etc/uwsgi/apps-enabled/cyberpdx.ini
cd /var/www/html/cyberpdx/www
virtualenv env --no-site-packages
(/bin/bash -c "source env/bin/activate; pip3 install flask lockfile pexpect")
touch /tmp/cyberpdx.sock
chown -R www-data /tmp/cyberpdx.sock
chown -R $SUDO_USER:www-data /var/www/html
chmod -R g+rwX /var/www/html
service nginx restart
service uwsgi restart
