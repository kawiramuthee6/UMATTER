from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the REPORT feature
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # Handle the report submission here
        pass
    return render_template('report.html')

# Route for the STATUS UPDATE feature
@app.route('/status_update', methods=['GET', 'POST'])
def status_update():
    if request.method == 'POST':
        # Handle the status update submission here
        pass
    return render_template('status_update.html')

# Route for the SUPPORT feature
@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        # Handle the support request here
        pass
    return render_template('support.html')

# Route for the FOLLOW-UP feature
@app.route('/follow_up', methods=['GET', 'POST'])
def follow_up():
    if request.method == 'POST':
        # Handle the follow-up request here
        pass
    return render_template('follow_up.html')

if __name__ == '__main__':
    app.run(debug=True)