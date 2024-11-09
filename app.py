from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'library.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')

# Initialize the database when the app runs
init_db()

# Route to view all books
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=books)

# Route to add a new book
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

# Route to delete a book
@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
