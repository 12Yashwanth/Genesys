from flask import Flask,render_template,request,redirect,session
import sqlite3

def init_db():
    conn=sqlite3.connect('contact.db')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

app=Flask(__name__)
app.secret_key='secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        """print("Received contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")"""
        # Store the contact form data in the database
        conn=sqlite3.connect('contact.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        return redirect('/contact')           #changes Post to Get request and redirects to the same page
    
    return render_template('contact.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/admin')
def admin():
    if not session.get("admin"):
        return redirect('/login')
    
    conn=sqlite3.connect('contact.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts=cursor.fetchall()
    conn.close()

    return render_template('admin.html', contacts=contacts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='admin' and password=='1234':
            session["admin"]=True   #This is used to set a session variable "admin" to True, indicating that the user has successfully logged in as an admin. This variable can be checked in other routes (like /admin) to determine if the user has the necessary permissions to access certain pages or perform specific actions.
            return redirect('/admin')
        
    return render_template('login.html')

@app.route('/services')
@app.route('/ai-projects')
@app.route('/products')
@app.route('/about')
@app.route('/careers')
def placeholder():
    return render_template('progress.html')

init_db()
