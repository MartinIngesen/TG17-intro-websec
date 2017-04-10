from flask import Flask, render_template, request, redirect, flash, url_for
from sqlite3 import dbapi2 as sqlite3
app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect('./database.db')
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = connect_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return redirect('/')

    init_db()
    
    username = request.form['username']
    password = request.form['password']

    db = connect_db()

    query = 'SELECT * FROM users WHERE username = \"' + username + '\" AND password = \"' + password + '\"'
    data = db.execute(query)

    user = data.fetchall()

    if len(user) == 0:
        flash("Incorrect credentials")
        return redirect(url_for('index'))
    db.close()

    return render_template('admin.html', username=user[0][1])

app.secret_key = "Onomatopoetikon"
if __name__ == "__main__":
    app.run()
