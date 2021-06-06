from flask import Flask
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config["MYSQL_DATABASE_USER"] = 'dthaa'
app.config["MYSQL_DATABASE_PASSWORD"] = 'dung12345'
app.config["MYSQL_DATABASE_DB"] = 'moodify'
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

# cursor.execute("SELECT * from user")
# data = cursor.fetchone()