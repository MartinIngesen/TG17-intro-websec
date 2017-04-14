from flask import Flask, render_template, request, redirect, flash, url_for, make_response
from sqlite3 import dbapi2 as sqlite3
app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect('./database.db')
    rv.row_factory = sqlite3.Row
    return rv

@app.before_first_request
def init_db():
    """Initializes the database."""
    db = connect_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_user_by_id(id):
    db = connect_db()
    data = db.execute('SELECT * FROM users WHERE id = ?', id)
    user = data.fetchone()
    db.close()
    return user

def get_entries():
    db = connect_db()
    data = db.execute('SELECT * FROM guestbook')
    entries = data.fetchall()
    db.close()
    return entries

@app.route("/")
def index():
    if request.cookies.get('userid'):
        return redirect(url_for('admin'))
    else:
        return render_template('index.html')

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userid', '', expires=0)
    return resp

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        userid = request.cookies.get('userid')
        if userid:
            user = get_user_by_id(userid)
            entries = get_entries()
            return render_template('admin.html', username=user[1], entries=entries)
        else:
            return redirect(url_for('index'))

    username = request.form['username']
    password = request.form['password']

    db = connect_db()

    query = 'SELECT * FROM users WHERE username = ? AND password = ?'
    data = db.execute(query, [username, password])

    user = data.fetchone()

    if not user:
        flash("Incorrect credentials")
        return redirect(url_for('index'))

    db.close()

    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('userid', str(user[0]))
    return resp

@app.route('/add', methods=['POST'])
def add_entry():
    db = connect_db()
    db.execute('insert into guestbook (entry) values (?)', [request.form['text']])
    db.commit()
    db.close()
    return redirect(url_for('admin'))

app.secret_key = "Onomatopoetikon"
if __name__ == "__main__":
    app.run()
