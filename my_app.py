import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

# ...

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    login = conn.execute('SELECT * FROM login').fetchall()
    conn.close()
    return render_template('index.html', login=login)


@app.route('/success/<name>')
def success(name):
    return render_template("home.html", name=name)
# ...

@app.route('/login/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']

        if not name:
            flash('name is required!')
        elif not mail:
            flash('mail is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO login (name, mail) VALUES (?, ?)',
                         (name, mail))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)






