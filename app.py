from flask import Flask, render_template, request
import sqlite3
import datetime

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods = ["get", "post"])
def main():
    r = request.form.get('q')
    current_time = datetime.datetime.now()
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute('INSERT INTO user (name, timestamp) VALUES (?, ?)', (r, current_time))
    conn.commit()
    c.close()
    conn.close()
    return render_template('main.html', r=r)

@app.route('/store_money', methods = ["get", "post"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money', methods = ["get", "post"])
def transfer_money():
    return render_template('transfer_money.html')

@app.route('/admin', methods = ["get", "post"])
def admin():
    return render_template('admin.html')

@app.route('/viewDB', methods = ["get", "post"])
def viewDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user')
    r = ""
    for row in c.fetchall():
        r += str(row) + "\n"
    c.close()
    conn.close()
    return render_template('viewDB.html', r = r)

@app.route('/delDB', methods = ["get", "post"])
def delDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute('DELETE FROM user')
    conn.commit()
    c.close()
    conn.close()
    return render_template('delDB.html')

if __name__=='__main__':
    app.run()