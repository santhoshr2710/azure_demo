# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def home():
    # Render the 'index.html' template with a custom message
    return render_template('index.html', message='Welcome to My Flask App!')

# Run the application if this script is executed
if __name__ == '__main__':
    # Run the app on http://127.0.0.1:5000/
    app.run(debug=True)
