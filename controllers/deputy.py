from flask import render_template, session, request
import MySQLdb
from __main__ import app

from models.model import db, Schedule

def deputy_route(app):
    @app.route('/deputy', methods = ['GET','POST'])
    def deputy():
        em = session['email']
        info = 'deputy'
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
        cursor = conn.cursor()
        # Query execute
        if session['email'] != 'sameer@gmail.com':
            cursor.execute('SELECT * FROM user WHERE email = %s', (session['email'],))
        else:
            cursor.execute('SELECT * FROM admin WHERE email = %s', (session['email'],))
        # Matched row in 'user'
        user = cursor.fetchone()
        if user != None:
            if user[2] == 'Deputy Warden' or session['email'] == 'sameer@gmail.com':
                failed= ""
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM schedule Where type = %s',('Not Assigned',))
                # Matched row in 'user'
                user = cursor.fetchall()
                if user:
                    if request.method == 'POST':

                        if 'Modify' == request.form.get('btn'):
                            email = request.form.get('email')
                            user = Schedule.query.filter_by(email=email).first()
                            if user:
                                user.type = request.form.get('type')
                                user.shift = request.form.get('shift')
                                if request.form.get('shift') == 'Day':
                                    user.time = '8AM - 3PM'
                                else:
                                    user.time = '9PM - 12AM'
                                
                                db.session.commit()
                                # Database connect
                                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                                cursor = conn.cursor()
                                # Query execute
                                cursor.execute('SELECT * FROM schedule Where type = %s',('Not Assigned',))
                                # Matched row in 'user'
                                user = cursor.fetchall()
                                if not user:
                                    user = "Nothing"
                                failed="Changed!"
                        elif '🍳' == request.form.get('btn'):
                            email = request.form.get('email')
                            user = Schedule.query.filter_by(email=email).first()
                            # Database connect
                            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                            cursor = conn.cursor()
                            # Query execute
                            cursor.execute('SELECT * FROM schedule WHERE email = %s', (email,))
                            # Matched row in 'user'
                            user = cursor.fetchall()
                else:
                    user = 'Nothing'

                return render_template('deputy.html',user=user,failed=failed,info=info, em=em)
            else:
                return render_template('error.html')
        else:
            return render_template('error.html')
        
 # End