This is the source distribution for the challenges and urban race used in CyberDiscovery at Portland State University in 2015.

Challenges/      => Directory containing the first 24 puzzles
LectureHandouts/ => For the examples in class
UrbanRace/       => Urban Race puzzles and the Twitter bot used to run race
www/             => Web site for handling puzzle solutions

To setup the web site:
Clone the git repository into a place that you will run from.  For example,
/var/www/html.  If you don't have git....
        sudo apt-get install git
        cd /var/www/html
        git clone https://<username>@bitbucket.org/wuchangfeng/cyberd_crypto_2015.git
                or
        git clone https://<username>@bitbucket.org/wuchangfeng/cyberd_crypto_2015.git <dirname>

The files assume that <dirname> is cyberd.

To ensure all of the necessary software is available, install the following
packages and the extras it asks for.  They are necessary for 32-bit compiling,
the unpacking challenges, and the Python-Flask web interface....
        sudo apt-get install python-pip
        sudo apt-get install python-virtualenv
        sudo apt-get install libapache2-mod-wsgi
To create the Python virtualenv, do:
        cd www
        mkdir env
        virtualenv env
        source env/bin/activate

Within the environment, install flask, lockfile, and pexpect using
these commands...
        pip install flask
        pip install lockfile

To configure the web site,
        Edit www/login.py to configure users and passwords (Apologies in advance for this.
             Would love to do something more clever like OAuth here)
        Move www/etc/apache2/sites-available/cyberd.conf to the appropriate
                place (/etc/apache2/sites-available/cyberd.conf) and
                edit the file to reflect your local configuration
                (i.e. ServerName, ServerAlias, WSGI path settings)
        Edit www/app.wsgi to point to where your web files are

        Enable the site
                sudo a2enmod wsgi (if necessary)
                sudo a2ensite cyberd
                sudo service apache2 restart

        If you have permission errors, ensure that your directories
                are readable by apache2 (www-data)

If you have any questions, wuchang at pdx.edu