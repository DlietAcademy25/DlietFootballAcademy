from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json, os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class for Flask-Login acount management

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Dummy user database
users = {'admin': {'password': 'adminpass'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(id=username)
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    with open('data/events.json', 'r') as f:
        events = json.load(f)
    return render_template('admin_dashboard.html', events=events)

@app.route('/admin_dashboard/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        new_event = {
            "title": request.form['title'],
            "date": request.form['date'],
            "description": request.form['description'],
            "participants": int(request.form['participants'])
        }
        with open('data/events.json', 'r') as f:
            events = json.load(f)
        events.append(new_event)
        with open('data/events.json', 'w') as f:
            json.dump(events, f, indent=4)
        return redirect(url_for('admin_dashboard'))
    return render_template('add_event.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    with open('data/events.json', 'r') as f:
        events = json.load(f)
    return render_template('events.html', events=events)

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle the form submission, such as saving to a database or sending an email
        flash('Your message has been sent successfully')
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/get_involved')
def get_involved():
    return render_template('get_involved.html')

@app.route('/schedule')
def schedule():
    # Render the schedule page
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=False)
    
