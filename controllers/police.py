from flask import render_template, session, request
import MySQLdb
from __main__ import app

from models.model import db, Request, Needs

def police_route(app):
    @app.route('/police', methods = ['GET','POST'])
    def police():
        if request.method == 'POST':
            if request.form.get('shift'):
                req="Request Send!"
                shift = request.form.get('shift')
                email = session['email']
                reason = request.form.get('reason')
                existing_user = Request.query.filter_by(email=email).first()
                if existing_user:
                    req="Already Requested!"
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM schedule WHERE email = %s', (session['email'],))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # Create a new tuple with the additional element "Police"
                    user = user[0] + ('Police',)
                    # Create a double tuple with the inner tuple
                    user = (user,)
                    return render_template('police.html',user=user,req=req,email=session['email'])
                else:
                    entry = Request(shift=shift, email=email, reason=reason,role = 'Police')
                    db.session.add(entry)
                    db.session.commit()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM schedule WHERE email = %s', (session['email'],))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # Create a new tuple with the additional element "Police"
                    user = user[0] + ('Police',)
                    # Create a double tuple with the inner tuple
                    user = (user,)
                    return render_template('police.html',user=user,req=req,email=session['email'])
            else:
                req="Request Send!"
                needs = request.form.get('needs')
                email = session['email']
                entry = Needs(needs = needs, status="pending")
                db.session.add(entry)
                db.session.commit()
                # Database connect
                conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                cursor = conn.cursor()
                # Query execute
                cursor.execute('SELECT * FROM schedule WHERE email = %s', (session['email'],))
                # Matched row in 'user'
                user = cursor.fetchall()
                # Create a new tuple with the additional element "Police"
                user = user[0] + ('Police',)
                # Create a double tuple with the inner tuple
                user = (user,)
                return render_template('police.html',user=user,req=req,email=session['email'])
        else:
            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
            cursor = conn.cursor()
            # Query execute
            cursor.execute('SELECT * FROM user WHERE email = %s', (session['email'],))
            # Matched row in 'user'
            user = cursor.fetchone()
            if user != None:
                if user[2] == 'Police': 
                        # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM schedule WHERE email = %s', (session['email'],))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM schedule WHERE email = %s And type = %s' , (session['email'],'Not Assigned'))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # Create a new tuple with the additional element "Cleaner"
                    if user:
                        cursor.execute('SELECT * FROM user WHERE email = %s', (session['email'],))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        user = user[0] + ('Police',)
                        # Create a double tuple with the inner tuple
                        user = (user,)
                        return render_template('police.html',user=user,req="Your Work Schedule Will Be Updated Soon!",email=session['email'])
                    else:
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM schedule WHERE email = %s' , (session['email'],))
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        user = user[0] + ('Police',)
                        # Create a double tuple with the inner tuple
                        user = (user,)
                        return render_template('police.html',user=user,req="You Can't Request Again If You Already Have A Pending Request!",email=session['email'])
                else:
                    return render_template('error.html')
            else:
                return render_template('error.html')
            

 # End