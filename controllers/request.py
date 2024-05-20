from flask import render_template, session, request
import MySQLdb
from models.model import db, Schedule, Request
from __main__ import app

def request_route(app):
    @app.route('/req', methods = ['GET','POST'])
    def req():
        param1 = request.args.get('param1')
        if session['email'] != 'sameer@gmail.com':
            return render_template('error.html')
        elif request.method == 'POST':
            btn = request.form.get('btn')
            if request.form.get('shift'):
                email = request.form.get('email')
                shift = request.form.get('shift')
                staff = request.form.get('staff')
            else:
                needsId = request.form.get('id')
            if btn == 'accept':
                if request.form.get('id'):
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    cursor.execute('UPDATE needs SET status = %s WHERE id = %s', ('accepted', needsId))
                    conn.commit()
                    # Query execute
                    cursor.execute('SELECT * FROM needs Where status = %s', ("pending",))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    return render_template('request.html',user=user, prisoner = "prisoner")
                else:
                    user = Schedule.query.filter_by(email=email).first()
                    if user:
                        user.shift = request.form.get('shift')
                        if shift == 'Day':
                            user.time = '8AM - 3PM'
                        else:
                            user.time = '9PM - 12AM' 
                        db.session.commit()
                    user = Request.query.filter_by(email=email).first()
                    if user:
                        db.session.delete(user)
                        db.session.commit()
                    if param1 == "Guard" or staff == "Police":
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Police',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
                    elif param1 == "Chef" or staff == 'Chef':
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Chef',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
                    else:
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Cleaner',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
            else:
                if request.form.get('id'):
                    needsId = request.form.get('id')
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    cursor.execute('UPDATE needs SET status = %s WHERE id = %s', ('rejected', needsId))
                    conn.commit()
                    # Query execute
                    cursor.execute('SELECT * FROM needs Where status = %s', ("pending",))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    return render_template('request.html',user=user, prisoner = "prisoner")
                else:
                    user = Request.query.filter_by(email=email).first()
                    if user:
                        db.session.delete(user)
                        db.session.commit()
                    if param1 == "Guard" or staff == "Police":
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Police',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
                    elif param1 == "Chef" or staff == "Chef":
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Chef',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
                    else:
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM request Where role = %s', ('Cleaner',))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        return render_template('request.html',user=user)
        else:
            if param1 == "Guard":
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM request Where role = %s', ('Police',))
                # Matched row in 'user'
                user = cursor.fetchall()
                return render_template('request.html',user=user)
            elif param1 == "Chef":
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM request Where role = %s', ('Chef',))
                # Matched row in 'user'
                user = cursor.fetchall()
                return render_template('request.html',user=user)
            elif param1 == "Prisoner":
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM needs WHERE status = %s', ('pending',))
                # Matched row in 'user'
                user = cursor.fetchall()
                return render_template('request.html',user=user,prisoner = "prisoner")
            else:
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM request Where role = %s', ('Cleaner',))
                # Matched row in 'user'
                user = cursor.fetchall()
                return render_template('request.html',user=user)
            
 # End