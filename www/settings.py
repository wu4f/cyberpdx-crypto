import os

# Used to sign cookies
if 'SECRET_KEY' in os.environ:
    secret_key = os.environ['SECRET_KEY']
else:
    secret_key = b'\xda$\x04\x00\x0f\x83#l\x98\xc8f[4\x05!['

# Look to pull admin password from environment variables.
#   Set it to default pdxctf if not given any
if 'ADMIN_PASS' in os.environ:
    admin_pass = os.environ['ADMIN_PASS']
else:
    admin_pass = 'cyberpdx'
