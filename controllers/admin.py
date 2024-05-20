from flask import render_template, session, request, redirect, url_for
import MySQLdb
import hashlib
from __main__ import app

def admin_route(app):
    @app.route('/admin', methods = ['GET','POST'])
    def admin():
        failed = ""
        session['email'] = ""
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            # Database connect
            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
            cursor = conn.cursor()
            # Query execute
            cursor.execute('SELECT * FROM admin WHERE `email` = %s', (email,))
            # Matched row in 'user'
            user = cursor.fetchone()

            if user is not None:
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                cursor.execute('SELECT * FROM admin WHERE password = %s And email = %s', (hashed_password,email))
                user1 = cursor.fetchone()
                if user1 is not None:
                    session['email'] = user[1]
                    return redirect(url_for('adminDash'))
                else:
                    failed = "Password Does Not Matched!"
                    # return redirect(url_for('admin'))
            else:
                failed = "Email Not Found!"
        return render_template('admin.html',failed=failed)
    
 # End