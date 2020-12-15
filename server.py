from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

class Student:
    def __init__(self, name, pw):
        self.name = name
        self.pw = pw

student_vector = []

app = Flask(__name__)

@app.route('/')
@app.route('/login/check', methods=['GET','POST'])
def Login():
    
    if request.method == "POST":
        username = request.form['sID']
        password = request.form['PW']

        if not (username and password):
            flash("Username or Password cannot be empty")
            print("Username or Password cannot be empty")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        db = sqlite3.connect("todo_list.db")
        db.row_factory = sqlite3.Row
        item = db.execute("select PW from Student where sID=?",(int(username),)).fetchone()
      
        if(item == None):
            flash("Invalid username or password")
            print("Invalid username or password")
            return redirect(url_for('Login'))
        elif(item[0] == password):
            flash("logged in")
            print("logged in")
            return redirect(url_for('home', sID=int(username)))
        else:
            flash("Invalid username or password")
            print("Invalid username or password")
            return redirect(url_for('Login'))

    return render_template('login.html')

@app.route('/home/<int:sID>', methods=['GET','POST'])
def home(sID):
    db = sqlite3.connect("todo_list.db")
    db.row_factory = sqlite3.Row
    
    if request.method == "POST":
        db2 = sqlite3.connect("todo_list.db")
        c = db2.cursor()
        db2.row_factory = lambda cursor, row: row[0]


        VAHs = db2.execute(
        'SELECT VAHName FROM VideoAndHomework, Class WHERE sID=? and VideoAndHomework.cID = Class.cID',(sID,)
        ).fetchall()
        Decisions = db2.execute(
            'SELECT Decision FROM VideoAndHomework, Class WHERE sID=? and VideoAndHomework.cID = Class.cID',(sID,)
        ).fetchall()
        count = 0
        for VAH in VAHs:
            
            #print(Decisions)
            if request.form.get(VAH):
                if Decisions[count] == 'Y':

                    c.execute(
                        """UPDATE VideoAndHomework set Decision='N' where VAHName=?""",(VAH,)
                    )
                    db2.commit()
                    print(count)
                    print("Y로 변경")
                elif Decisions[count] == 'N':

                    c.execute(
                        """UPDATE VideoAndHomework set Decision='Y' where VAHName=?""",(VAH,)
                    )
                    db2.commit()
                    print(count)
                    print("N으로 변경")
                #print(VAH)
            count = count + 1
        
        # Decisions = db.execute(
        #     'SELECT Decision FROM VideoAndHomework, Class WHERE sID=? and VideoAndHomework.cID = Class.cID',(sID,)
        # ).fetchall()
        # print(Decisions[0][0])
        db2.close()
        # submit = request.form["학기프로젝트"]
        # print(VAH)
        # print(submit)
        
        # db.execute(
        #     'UPDATE VideoAndHomework SET dicision = "Y" WHERE sID'
        # )

    items = db.execute(
        'SELECT VAHName, Class.cID,cName,Decision,DeadLine FROM VideoAndHomework, Class WHERE sID=? and VideoAndHomework.cID = Class.cID',(sID,)
    ).fetchall()

    
    db.close()
    return render_template('home.html', items= items)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run(host='127.0.0.1', port=5000)