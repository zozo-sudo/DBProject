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

@app.route('/home/<int:sID>')
def home(sID):
    db = sqlite3.connect("todo_list.db")
    db.row_factory = sqlite3.Row
    # items = db.execute(
    #     'select cName from Sugang, Class where Sugang.cID=Class.cID and sID=?',(sID,)
    # ).fetchall()
    items = db.execute(
        'select VAHName, VideoAndHomework.cID from VideoAndHomework where VideoAndHomework.cID in (select Sugang.cID from Sugang, Class where Sugang.cID=Class.cID and sID=?)',(sID,)
    )
    #db.close()
    return render_template('home.html', items= items)



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run(host='127.0.0.1', port=5000)