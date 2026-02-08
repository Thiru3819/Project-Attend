from flask import Flask, render_template
# import mysql.connector
app=Flask(__name__)

# db = mysql.connector.connect(host="localhost" ,user="admin" , passwd="Thiru@9600",database="college")
# dbcursor=db.cursor()
# dbcursor.execute("SELECT * FROM attendances ")
# result=dbcursor.fetchall()

    
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
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

