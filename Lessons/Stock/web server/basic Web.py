# Import the Flask module from the flask package
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def home():
    # Return a simple HTML page
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Basic Web Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a basic HTML page served by Flask.</p>
    </body>
    </html>
    '''

# Check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True)