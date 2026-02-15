from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/services')
@app.route('/ai-projects')
@app.route('/products')
@app.route('/about')
@app.route('/careers')
def placeholder():
    return render_template('progress.html')
