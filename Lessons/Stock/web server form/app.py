from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    # Get the 'a' and 'b' parameters from the form
    a = request.form.get('a', type=float)
    b = request.form.get('b', type=float)
    
    # Check if the parameters are provided
    if a is None or b is None:
        return jsonify({'error': 'Please provide both "a" and "b" parameters.'}), 400
    
    # Compute the sum
    result = a + b
    
    # Return the result as a JSON response
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
