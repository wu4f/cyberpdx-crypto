This is the source distribution for the challenges and urban race used in CyberPDX at Portland State University.

Challenges/      => Directory containing the first 24 puzzles
LectureHandouts/ => For the examples in class
UrbanRace/       => Urban Race puzzles and the Twitter bot used to run race
www/             => Web site for handling puzzle solutions

For generating the challenges, also install the following:
	pip install pillow	(3.2.0)
	pip install code128 	(0.3)
	pip install py-enigma	(0.1)
	pip install PyQRCode	(1.2.1)
	pip install pyBarcode	(0.7)
	pip install pypng	(0.0.18)

To configure the web site, the installation script will integrate the
application with nginx via uwsgi, then obtain a TLS certificate from Let's
Encrypt.  To install:

1. Bring up a Ubuntu 18.04 instance.

2. Point the DNS name you'd like to use to the IP address of the instance.

3. Clone this repository and rename the directory.

4. cd into directory

5. sudo ./install.sh <dns_name>

6. Edit www/login.py to configure users and passwords

7. Restart systemctl service to load new users

If you have any questions, wuchang at pdx.edu
