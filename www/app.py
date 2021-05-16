#!/usr/bin/env python
import flask
import settings
from main import Main
from login import Login
from solve import Solve
from score import Score

app = flask.Flask(__name__)

app.secret_key = settings.secret_key

app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=['GET','POST'])

app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=['GET', 'POST'])

app.add_url_rule('/solve/',
                 view_func=Solve.as_view('solve'),
                 methods=["GET", "POST"])

app.add_url_rule('/score/',
                 view_func=Score.as_view('score'),
                 methods=["GET"])

app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
    #app.run(host='127.0.0.1',port=5001)
