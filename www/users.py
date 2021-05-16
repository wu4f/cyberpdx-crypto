# users = {
#         'wuchang': ['9999', 'Wu'],
#         'cyberpdx': ['crypto', 'Demo'],
#         'cdpdx1': ['znuwha01', 'Capital'],
#         'cdpdx3': ['ioknjl03', 'Lincoln'],
#         'cdpdx4': ['alnqkc04', 'Madison'],
#         'cdpdx5': ['fzwvsq05', 'Skyview'],
#         'cdpdx6': ['yxehal06', 'St.Marys'],
#         'cdpdx7': ['okavsg07', 'SST'],
#         'cdpdx9': ['qrghpt09', 'Tualatin'],
#         'cdpdx10': ['puxstq10', 'Village'],
#         'cdpdx11': ['uxstqp11', 'OregonCity'],
#         'cdpdx12': ['xstpuq12', 'ParkRoseGrant']
# }
"""
+------------+------------------+
| Username   | PassHash         |
+============+==================+
| John Doe   | 1234             |
+------------+------------------+

This can be created with the following SQL (see bottom of this file):

    create table users (username text, passhash text);

"""
import sqlite3, csv
from passlib.hash import pbkdf2_sha256
import shlex, subprocess
import settings

DB_FILE = 'users.db'    # file for our Database

class Users():
    def __init__(self):
        # Make sure our database exists
        self.connection = sqlite3.connect(DB_FILE)
        cursor = self.connection.cursor()
        try:
            cursor.execute("select count(rowid) from users")
        except sqlite3.OperationalError:
            self.initializeUsers()

    def initializeUsers(self):
        cursor = self.connection.cursor()
        cursor.execute("create table users (username text, realname text, passhash text)")
        self.addUser('admin', settings.admin_pass)
        for i in range(10):
            self.addUser(f'demo{i}','malware')

    def addUser(self, username, password):
        """
        Checks to see user does not exist, then adds user
        Each row contains: name, email, date, message
        :param username: String
        :param password: String
        :return: True if successful, False if user exists already
        """
        cursor = self.connection.cursor()
        params = {'username':username}
        cursor.execute("SELECT username FROM users WHERE username=(:username)", params)
        res = cursor.fetchall()
        if len(res) == 0:
            passhash = pbkdf2_sha256.hash(password)
            params = {'username':username, 'passhash':passhash}
            #print(f'Adding {username} with name {realname}, password {password} and hash {passhash}')
            cursor.execute("insert into users (username, passhash) VALUES (:username, :passhash)", params)
            self.connection.commit()
            subprocess.Popen(shlex.split(f'/bin/mkdir -p static/obj/{username}/solved'))
            return True
        else:
            return False

    def checkUser(self, username, password):
        """
        Checks credentials
        :param username: String
        :param password: String
        :return: True if successful, False if user exists already
        :raises: Database errors on connection and insertion
        """
        params = {'username':username}
        cursor = self.connection.cursor()
        cursor.execute("select passhash from users WHERE username=(:username)", params)
        res = cursor.fetchall()
        if len(res) != 0:
            hash = res.pop()[0]
            if (pbkdf2_sha256.verify(password, hash)):
                return True
        return False

    def changeUser(self, username, password):
        """
        Checks credentials
        :param username: String
        :param password: String
        :return: True if successful, False if user exists already
        :raises: Database errors on connection and insertion
        """
        passhash = pbkdf2_sha256.hash(password)
        params = {'username':username, 'passhash':passhash}
        cursor = self.connection.cursor()
        cursor.execute("update users SET passhash = (:passhash) WHERE username=(:username)", params)
        self.connection.commit()
        #print(f'Changing {username} with {password} and hash {passhash}')
        return True

    def importUsers(self, filename):
        """
        :param filename: String
        """
        f = open(filename, 'r')
        reader = csv.DictReader(f, fieldnames = ('username','password'))
        imported = []
        notimported = []
        cnt = 0;
        for row in reader:
            if self.addUser(row['username'],row['password']):
                imported.append((row['username'],row['password']))
                cnt = cnt + 1
            else:
                notimported.append((row['username'],row['password']))
        return imported, notimported

    def dumpUsers(self):
        """
        Gets all users from the database
        :return: List of users
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT username FROM users")
        res = cursor.fetchall()
        return [ i[0] for i in res ]

    def resetCTF(self):
        """
        Reset the CTF
        """
        cursor = self.connection.cursor()
        cursor.execute("drop table users")
        subprocess.Popen(shlex.split(f'/bin/rm -rf static/obj/*'))
        self.initializeUsers()
        return True
