from flask import Flask, render_template
import mysql.connector
import pandas as pd
app=Flask(__name__)

db = mysql.connector.connect(host="localhost" ,user="admin" , passwd="Thiru@9600",database="college")
dbcursor=db.cursor()
dbcursor.execute("SELECT * FROM attendances ")
result=dbcursor.fetchall()
df=pd.DataFrame(result)
print(df)
    
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/login")
def login():
    return render_template("register.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",data=result)
    



if __name__=="__main__":
    app.run(debug=True)  