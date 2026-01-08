from flask import Flask, request, session, redirect, url_for,render_template
from casinoproject.usermanagement import checklogin
from casinoproject.usercreate import createuser
from casinoproject.gameinfo import showbalance
import sqlite3


app = Flask(__name__)

app.secret_key = 'casinobadsecretkey'

@app.route("/")
def frontpage():
    return render_template('index.html')

@app.route("/loginuser")
def loginpage():
    return render_template("login.html")

@app.route("/last5games")
def last5games():
    if 'username' in session:       
        connect = sqlite3.connect('./casino.db')
        cursor = connect.cursor()
        cursor.execute(f"""SELECT P1_Outcome, P2_Outcome, P3_Outcome, P4_Outcome, P5_Outcome, playernumber FROM Game_History WHERE username = '{session['username']}' ORDER BY RecordID ASC LIMIT 5 """)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))
                for row in cursor.fetchall()]
        return render_template("last_5_games.html", rows = data)
    else:
        return redirect('/login')
        


@app.route("/profilestats")
def profilestats():
    if 'username' in session:
        connect = sqlite3.connect('./casino.db')
        cursor = connect.cursor()
        cursor.execute(f"""SELECT credits, gameswon, gameslost FROM users WHERE username = '{session['username']}' """)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))  
                for row in cursor.fetchall()]
        return render_template("user_stats.html", rows = data)
    else:
        return redirect('/login')
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/')

@app.route("/registeruser")
def registerpage():
    return render_template("register.hmtl")

@app.route("/login", methods=['GET','POST'])
def login():
    """
    Login function sets an errorMsg which gets rendered down on the page. 
    """
    errorMsg = None  # Error if we fail to login. 
    if request.method == 'POST':
        # Save the form data to the session object
        username = request.form['username']
        password = request.form['password']
        success, message, name = checklogin(username, password)
        if success:
            session['username'] = name
            return redirect('/')
        else:
            errorMsg = message # Set an Error message if we fail to login, this then gets passed down onto the page.  

    return render_template('login.html',errorMsg = errorMsg)


@app.route("/register", methods=['GET','POST'])
def register():
    """
     Allows a user to register into the system. 

    """
    registerMessage = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, message = createuser(username, password)
        if success:
            session['username'] = username
            return redirect('/profilestats')
        else:
            registerMessage = message
            
        
    return render_template("register.html",registerMessage = registerMessage)


    if __name__ == '__main__':
        app.run(debug=True)
    
