"""
Login Screen Application
========================
A simple Flask login screen built using the Spec-Driven Development approach.
Credentials: admin / admin (can be changed via forgot-password reset flow)

Run: python app.py
Visit: http://127.0.0.1:1234
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
from datetime import datetime, timedelta

# Flask app setup — template folder points to templates/html/
app = Flask(
    __name__,
    template_folder='templates/html',
    static_folder='static'
)

# Secret key for session management
app.secret_key = 'speckit-login-secret-key'

# Mutable credentials — stored in-memory, resets on app restart
credentials = {
    'admin': 'admin'
}

# In-memory reset token storage: { username: { 'token': '123456', 'expires': datetime } }
reset_tokens = {}


@app.route('/')
def home():
    """Redirect root to login page."""
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Display login form and handle authentication."""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # Validate credentials
        if username in credentials and credentials[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """Display dashboard for authenticated users."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=session.get('username'))


@app.route('/logout')
def logout():
    """Clear session and redirect to login."""
    session.clear()
    return redirect(url_for('login'))


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Display forgot-password form and generate reset token."""
    token = None

    if request.method == 'POST':
        username = request.form.get('username', '')

        if username not in credentials:
            flash('Username not found.', 'error')
        else:
            # Generate a 6-digit reset token
            token = str(random.randint(100000, 999999))
            reset_tokens[username] = {
                'token': token,
                'expires': datetime.now() + timedelta(minutes=5)
            }

    return render_template('forgot_password.html', token=token)


@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    """Display reset-password form and handle password update."""
    if request.method == 'POST':
        token = request.form.get('token', '').strip()
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Find the matching token
        matched_username = None
        for username, data in reset_tokens.items():
            if data['token'] == token:
                matched_username = username
                break

        if matched_username is None:
            flash('Invalid reset token.', 'error')
        elif datetime.now() > reset_tokens[matched_username]['expires']:
            # Token has expired — remove it
            del reset_tokens[matched_username]
            flash('Reset token has expired.', 'error')
        elif new_password != confirm_password:
            flash('Passwords do not match.', 'error')
        elif not new_password:
            flash('Password cannot be empty.', 'error')
        else:
            # Update the password and clean up the token
            credentials[matched_username] = new_password
            del reset_tokens[matched_username]
            flash('Password reset successful. Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('reset_password.html')


if __name__ == '__main__':
    app.run(debug=True, port=1234)
