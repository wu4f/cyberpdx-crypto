import sys
import site
sys.path.insert(0,'/var/www/html/cyberd/www')
site.addsitedir('/var/www/html/cyberd/www/env/lib/python2.7/site-packages')
activate_this = '/var/www/html/cyberd/www/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
