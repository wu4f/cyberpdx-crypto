# Installs on Google Cloud Platform's Compute Engine for Ubuntu 16.04 LTS
# Takes the site name as an argument
cd /var/www/html
chown -R $SUDO_USER .
git clone https://wuchangfeng@bitbucket.org/wuchangfeng/cyberd_crypto_2016.git
cd /var/www/html/
mv cyberd_crypto_2016 cyberd
cd cyberd
mv etc/nginx/sites-available/cyberd /etc/nginx/sites-available/cyberd
mv etc/nginx/sites-enabled/cyberd /etc/nginx/sites-enabled/cyberd
cd /var/www/html/cyberd
mv etc/uwsgi/apps-available/cyberd.ini /etc/uwsgi/apps-available/cyberd.ini
mv etc/uwsgi/apps-enabled/cyberd.ini /etc/uwsgi/apps-enabled/cyberd.ini
cd /var/www/html/cyberd/www
virtualenv env --no-site-packages
(/bin/bash -c "source env/bin/activate; pip3 install flask lockfile pexpect")
touch /tmp/cyberd.sock
chown -R www-data /tmp/cyberd.sock
chown -R $SUDO_USER:www-data /var/www/html
chmod -R g+rwX /var/www/html
service nginx restart
service uwsgi restart
