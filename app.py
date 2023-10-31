from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mydatabase'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
