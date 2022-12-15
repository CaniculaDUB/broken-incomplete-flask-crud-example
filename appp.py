from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change these details to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = '34.67.56.128'
mysql.init_app(app)

@app.route("/add") #Add Student
def add():
  name = request.args.get('name')
  email = request.args.get('email')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s=f"INSERT INTO students(studentName, email) VALUES('{name}','{email}')" # kludge - use stored proc or params
  cur.execute(s)
  mysql.connection.commit()

  return f"<h1>Successs</h1>" # Really? maybe we should check!

@app.route("/delete") #DeleteStudent
def delete():
  name = request.args.get('name')
  cur = mysql.connection.cursor()
  s = f"DELETE FROM students where studentName='{name}'"
  print(s)
  cursor.execute(s)
  mysql.connection.commit()
  
  return f"<h1>Delete</h1>"
  
@app.route("/") #Default - Show Data
def read(): # Name of the method
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM students''')  # execute an SQL statment
  rv = cur.fetchall()  # Retreive all rows returend by the SQL statment
  Results = []
  html = ""
  for row in rv:  # Format the Output Results and add to return string
      Result = {}
      Result['Name'] = row[0].replace('\n', ' ')
      Result['Email'] = row[1]
      Result['ID'] = row[2]
      html = html + (f"<tr style='border: 1px solid blue'><th  style='border: 1px solid blue'>{Result['Name']}</th> <th style='border: 1px solid blue'>{Result['Email']}</th></tr> <br>")
  html = f"<table style='border: 1px solid blue'><tr style='border: 1px solid blue'><th  style='border: 1px solid blue'>Name</th><th style='border: 1px solid blue'>Email</th></tr>{html}</table>" 
  
  
  return html

if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080

