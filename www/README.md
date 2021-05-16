To run in testing mode....

cd ~/cyberpdx-crypto
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
cd www
gunicorn --bind :8000 --workers 1 --threads 8 app:app
