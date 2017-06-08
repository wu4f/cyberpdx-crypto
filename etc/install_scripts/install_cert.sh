#
# Certbot instructions
# These are untested instructions that will update nginx with the
#   certficate needed to do https.It will automatically generate
#   the certs and update the nginx configuration file.
#
add-apt-repository ppa:certbot/certbot -y
apt-get update
apt-get install certbot python-certbot-nginx -y
certbot --nginx
#...Follow instructions
