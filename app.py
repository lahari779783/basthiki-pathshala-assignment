from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Initialize SQLite DB
def init_db():
    conn = sqlite3.connect('volunteers.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            college TEXT NOT NULL,
            branch TEXT NOT NULL,
            year TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        branch = request.form['branch']
        year = request.form['year']
        contact = request.form['contact']

        conn = sqlite3.connect('volunteers.db')
        c = conn.cursor()
        c.execute("INSERT INTO volunteers (name, college, branch, year, contact) VALUES (?, ?, ?, ?, ?)",
                  (name, college, branch, year, contact))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    return render_template('register.html')

# Admin Panel
@app.route('/admin')
def admin():
    conn = sqlite3.connect('volunteers.db')
    c = conn.cursor()
    c.execute("SELECT id, name, college, branch, year, contact FROM volunteers")
    rows = c.fetchall()
    conn.close()

    volunteers = []
    for row in rows:
        volunteers.append({
            'id': row[0],
            'name': row[1],
            'college': row[2],
            'branch': row[3],
            'year': row[4],
            'contact': row[5]
        })

    return render_template('admin.html', volunteers=volunteers)

# Edit Volunteer
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect('volunteers.db')
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        branch = request.form['branch']
        year = request.form['year']
        contact = request.form['contact']

        c.execute('''
            UPDATE volunteers
            SET name = ?, college = ?, branch = ?, year = ?, contact = ?
            WHERE id = ?
        ''', (name, college, branch, year, contact, id))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    # GET request to pre-fill form
    c.execute("SELECT * FROM volunteers WHERE id = ?", (id,))
    row = c.fetchone()
    conn.close()

    if row:
        volunteer = {
            'id': row[0],
            'name': row[1],
            'college': row[2],
            'branch': row[3],
            'year': row[4],
            'contact': row[5]
        }
        return render_template('edit.html', volunteer=volunteer)
    else:
        return "Volunteer not found", 404

# Delete Volunteer
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    conn = sqlite3.connect('volunteers.db')
    c = conn.cursor()
    c.execute("DELETE FROM volunteers WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

#if __name__ == '__main__':
 #   app.run(debug=True)
