This is the source distribution for the challenges and urban race used in CyberPDX at Portland State University.

Challenges/      => Directory containing the first 24 puzzles
LectureHandouts/ => For the examples in class
UrbanRace/       => Urban Race puzzles and the Twitter bot used to run race
www/             => Web site for handling puzzle solutions

To setup the web site:
Clone the git repository into a place that you will run from.  For example,
/var/www/html.  If you don't have git....
        sudo apt-get install git
        cd /var/www/html
        git clone https://<username>@bitbucket.org/wuchangfeng/cyberpdx_crypto_2017.git
                or
        git clone https://<username>@bitbucket.org/wuchangfeng/cyberpdx_crypto_2017.git <dirname>

The files assume that <dirname> is cyberpdx.

To ensure all of the necessary software is available, install the following
packages and the extras it asks for.  They are necessary for 32-bit compiling,
the unpacking challenges, and the Python-Flask web interface....
        sudo apt-get install python-pip
        sudo apt-get install python-virtualenv
        sudo apt-get install libapache2-mod-wsgi
	sudo apt-get install libimage-exiftool-perl
To create the Python virtualenv, do:
        cd www
        mkdir env
        virtualenv env
        source env/bin/activate

Within the environment, install flask, lockfile, and pexpect using
these commands...
        pip install flask
        pip install lockfile

For generating the challenges, also install the following:
	pip install pillow	(3.2.0)
	pip install code128 	(0.3)
	pip install py-enigma	(0.1)
	pip install PyQRCode	(1.2.1)
	pip install pyBarcode	(0.7)
	pip install pypng	(0.0.18)

To configure the web site,
        Edit www/login.py to configure users and passwords (Apologies in advance for this.
             Would love to do something more clever like OAuth here)

        If using Apache,
          Move www/etc/apache2/sites-available/cyberpdx.conf to the appropriate
                place (/etc/apache2/sites-available/cyberpdx.conf) and
                edit the file to reflect your local configuration
                (i.e. ServerName, ServerAlias, WSGI path settings)
          Edit www/app.wsgi to point to where your web files are
          Enable the site
                sudo a2enmod wsgi (if necessary)
                sudo a2ensite cyberpdx
                sudo service apache2 restart
          If you have permission errors, ensure that your directories
                are readable by apache2 (www-data)
        If using nginx,
          Install scripts provided in etc/
          Then, to reload on a systemd do "sudo systemctl restart <service>"
If you have any questions, wuchang at pdx.edu
