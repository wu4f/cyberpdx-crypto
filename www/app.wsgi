import sys
import site
sys.path.insert(0,'/var/www/html/cyberpdx/www')
site.addsitedir('/var/www/html/cyberpdx/www/env/lib/python2.7/site-packages')
activate_this = '/var/www/html/cyberpdx/www/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
