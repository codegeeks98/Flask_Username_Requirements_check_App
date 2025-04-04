from flask import Flask, render_template, request

app = Flask(__name__)

# Fix: Add @ before app.route
@app.route('/')
def index():
    return render_template('index.html')

# Fix: Add methods=['GET'] and correct string in request.args.get()
@app.route('/report_page')    
def report_page():
    username = request.args.get('u_name')  # Fix: 'u_name' must be a string

    if not username:  # Fix: Handle None case to avoid errors
        return render_template('report.html', error="No username provided")

    # Check if it contains at least one lowercase letter
    has_lower = any(char.islower() for char in username)
    
    # Check if it contains at least one uppercase letter
    has_upper = any(char.isupper() for char in username)
    
    # Check if it ends with a number
    ends_with_digit = username[-1].isdigit()

    return render_template('report.html', has_lower=has_lower, has_upper=has_upper, ends_with_digit=ends_with_digit)

if __name__ == '__main__':
    app.run(debug=True)
