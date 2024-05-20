from flask import render_template, session, request
import MySQLdb
import hashlib
from models.model import db, User, Schedule
from __main__ import app

def staffDetails_route(app):
    @app.route('/staffDetails', methods = ['GET','POST'])
    def staffDetails():
        info = 'staff'
        if session['email'] != 'sameer@gmail.com':
            return render_template('error.html')
        else:
            failed= ""
            # Database connect
            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
            cursor = conn.cursor()
            # Query execute
            cursor.execute('SELECT * FROM user')
            # Matched row in 'user'
            user = cursor.fetchall()

            if request.method == 'POST':
                if 'Add' == request.form.get('btn'):
                    name = request.form.get('name')
                    email = request.form.get('email')
                    password = request.form.get('password')
                    role = request.form.get('occupation')

                    existing_user = User.query.filter_by(email=email).first()
                    if existing_user:
                        failed="Email already exists. Please choose a different email!"
                    else:
                        #hashed password
                        hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

                        entry = User(name=name, role=role, password=hashedPassword, email=email)
                        db.session.add(entry)
                        db.session.commit()

                        if role != "Deputy Warden":
                            entry = Schedule(name=name, email=email, type='Not Assigned', shift='Not Assigned', time='Not Assigned',role = role)
                            db.session.add(entry)
                            db.session.commit()
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM user')
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        failed="Added!"
                elif 'Modify' == request.form.get('btn'):
                    email = request.form.get('email')
                    role = request.form.get('occupation')
                    user = User.query.filter_by(email=email).first()
                    if user:
                        user.name = request.form.get('name')
                        user.password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest()
                        user.role = request.form.get('occupation')
                        db.session.commit()
                        user = Schedule.query.filter_by(email=email).first()
                        if role != 'Deputy Warden':
                            if user:
                                user.name = request.form.get('name')
                                user.role = request.form.get('occupation')
                                db.session.commit()
                            else:
                                name = request.form.get('name')
                                entry = Schedule(name=name, email=email, type='Not Assigned', shift='Not Assigned', time='Not Assigned',role = role)
                                db.session.add(entry)
                                db.session.commit() 
                        else:
                            if user:
                                db.session.delete(user)
                                db.session.commit()    
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM user')
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        failed="Changed!"
                elif '🍳' == request.form.get('btn'):
                    email = request.form.get('email')
                    user = User.query.filter_by(email=email).first()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                        
                else:
                    email = request.form.get('email')
                    user = User.query.filter_by(email=email).first()
                    if user:
                        db.session.delete(user)
                        db.session.commit()
                        user = Schedule.query.filter_by(email=email).first()
                        if user:
                            db.session.delete(user)
                            db.session.commit()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM user')
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # failed="Deleted!"

            return render_template('staffDetails.html',user=user,failed=failed,info=info)
        
 # End