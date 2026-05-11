#!/usr/bin/env python3
"""Minimal Flask app to test form submission."""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'test-key'

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Form Test</title>
    </head>
    <body>
        <h1>Test Form Submission</h1>
        <form action="/submit" method="POST">
            <div>
                <label for="escalation_id">Escalation ID:</label>
                <input type="text" name="escalation_id" id="escalation_id" required>
            </div>
            <div>
                <label for="customer">Customer:</label>
                <input type="text" name="customer" id="customer" required>
            </div>
            <div>
                <label for="problem_title">Problem Title:</label>
                <input type="text" name="problem_title" id="problem_title" required>
            </div>
            <div>
                <label for="engineer">Engineer:</label>
                <input type="text" name="engineer" id="engineer" required>
            </div>
            <button type="submit" id="submit-btn">Submit</button>
        </form>
        
        <script>
            document.querySelector('form').addEventListener('submit', function(e) {
                console.log('Form submission started');
                const submitBtn = document.getElementById('submit-btn');
                submitBtn.disabled = true;
                submitBtn.textContent = 'Submitting...';
            });
        </script>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    print("=== FORM SUBMITTED ===")
    print("Form data:", dict(request.form))
    
    # Validate required fields
    required_fields = ['escalation_id', 'customer', 'problem_title', 'engineer']
    for field in required_fields:
        if not request.form.get(field):
            return f"Error: {field} is required", 400
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Success</title>
    </head>
    <body>
        <h1>Form Submitted Successfully!</h1>
        <p>Escalation ID: ''' + request.form.get('escalation_id', '') + '''</p>
        <p>Customer: ''' + request.form.get('customer', '') + '''</p>
        <p>Problem: ''' + request.form.get('problem_title', '') + '''</p>
        <p>Engineer: ''' + request.form.get('engineer', '') + '''</p>
        <a href="/">Submit Another</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("Starting minimal Flask test app...")
    app.run(host='127.0.0.1', port=5003, debug=False)