from flask import Flask, render_template
import mysql.connector
app=Flask(__name__)

db = mysql.connector.connect(host="localhost" ,user="admin" , passwd="Thiru@9600",database="college")
dbcursor=db.cursor()
dbcursor.execute("SELECT * FROM attendances ")
result=dbcursor.fetchall()

    
@app.route("/")
def index():
    return render_template('index1.html')
@app.route("/replogin")
def replogin():
    return render_template("REP_LOGIN.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",data=result)


if __name__=="__main__":
    app.run(debug=True)  