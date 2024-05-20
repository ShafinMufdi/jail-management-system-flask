from flask import render_template, session, request, redirect, url_for
import MySQLdb
import hashlib
from __main__ import app

def login_route(app):
    @app.route('/login', methods = ['GET','POST'])
    def login():
        failed = ""
        session['email'] = ""
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            # Database connect
            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
            cursor = conn.cursor()
            # Query execute
            cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
            # Matched row in 'user'
            user = cursor.fetchone()
            if user is not None:
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                cursor.execute('SELECT * FROM user WHERE password = %s And email = %s', (hashed_password,email))
                user1 = cursor.fetchone()
                if user1 is not None:
                    session['id'] = user[0]
                    session['email'] = user[3]
                    if user[2] == "Cleaner":
                        return redirect(url_for('cleaner'))
                    elif user[2] == "Chef":
                        return redirect(url_for('chef'))
                    elif user[2] == "Deputy Warden":
                        return redirect(url_for('deputy'))
                    else:
                        return redirect(url_for('police'))
                else:
                    failed = "Password Does Not Match!"
            else:
                failed = "Email Not Found!"
            
        return render_template('login.html', failed=failed)
    
    
 # End