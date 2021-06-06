from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.php")

@app.route('/login')
def login():
    return render_template("Login.php")

@app.route('/angry')
def love():
    return render_template("angry.php")



if __name__ == "__main__":
    app.run(debug=True)