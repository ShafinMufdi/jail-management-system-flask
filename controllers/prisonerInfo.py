from flask import render_template, session, request
import MySQLdb
from models.model import db, Prisoner
from __main__ import app

def prisonerInfo_route(app):
    @app.route('/prisonerInfo', methods = ['GET','POST'])
    def prisonerInfo():
        info = 'prisoner'
        if session['email'] != 'sameer@gmail.com':
            return render_template('error.html')
        else:
            failed= ""
            # Database connect
            conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
            cursor = conn.cursor()
            # Query execute
            cursor.execute('SELECT * FROM prisoner')
            # Matched row in 'user'
            user = cursor.fetchall()

            if request.method == 'POST':
                if 'Add' == request.form.get('btn'):
                    cell1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                    name = request.form.get('name')
                    age = request.form.get('age')
                    birth = request.form.get('birth')
                    record = request.form.get('record')
                    # cell = request.form.get('cell')
                    year = request.form.get('year')
                    cell=''
                    for i in cell1:
                        for j in range(1,11):
                            cellCheck = str(j)+i
                            existing_user = Prisoner.query.filter_by(cell=cellCheck).first()
                            if existing_user:
                                continue
                            else:
                                break
                        if existing_user:
                            continue
                        else:
                            cell = cellCheck
                            break
                    if cell == '':
                        failed="Prison Is Full!"
                    else:
                        entry = Prisoner(name=name, age=age, birth=birth, record=record, cell=cell, year=year)
                        db.session.add(entry)
                        db.session.commit()
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM prisoner')
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        failed="Added!"
                elif 'Modify' == request.form.get('btn'):
                    cell = request.form.get('cell')
                    user = Prisoner.query.filter_by(cell=cell).first()
                    if user:
                        user.name = request.form.get('name')
                        user.age = request.form.get('age')
                        user.birth = request.form.get('birth')
                        user.record = request.form.get('record')
                        user.cell = request.form.get('cell')
                        user.year = request.form.get('year')
                        db.session.commit()
                        # Database connect
                        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                        cursor = conn.cursor()
                        # Query execute
                        cursor.execute('SELECT * FROM prisoner')
                        # Matched row in 'user'
                        user = cursor.fetchall()
                        failed="Changed!"
                elif '🍳' == request.form.get('btn'):
                    cell = request.form.get('cell')
                    user = Prisoner.query.filter_by(cell=cell).first()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM prisoner WHERE cell = %s', (cell,))
                    # Matched row in 'user'
                    user = cursor.fetchall()
                        
                else:
                    cell = request.form.get('cell')
                    user = Prisoner.query.filter_by(cell=cell).first()
                    if user:
                        db.session.delete(user)
                        db.session.commit()
                    # Database connect
                    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jailmanage')
                    cursor = conn.cursor()
                    # Query execute
                    cursor.execute('SELECT * FROM prisoner')
                    # Matched row in 'user'
                    user = cursor.fetchall()
                    # failed="Deleted!"

            return render_template('prisonerInfo.html',user=user,failed=failed,info=info)
        
 # End