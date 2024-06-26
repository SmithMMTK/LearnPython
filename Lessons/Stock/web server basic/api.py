from flask import Flask, request, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the API call to add two numbers
@app.route('/add', methods=['GET'])
def add():
    # Get the 'a' and 'b' parameters from the request
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    # Check if the parameters are provided
    if a is None or b is None:
        return jsonify({'error': 'Please provide both "a" and "b" parameters.'}), 400
    
    # Compute the sum
    result = a + b
    
    # Return the result as a JSON response
    return jsonify({'result': result})

# Check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True)
