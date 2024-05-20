from flask import session, render_template
from __main__ import app

def home_route(app):
    @app.route('/')
    @app.route('/home')
    def home():
        session['email'] = ""
        return render_template('home.html')
    
 # End