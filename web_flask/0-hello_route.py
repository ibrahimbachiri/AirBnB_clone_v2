from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define a route for '/airbnb-onepage/' that returns 'Hello HBNB!'
@app.route('/airbnb-onepage/')
def hello_hbnb():
    return 'Hello HBNB!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
