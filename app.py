import webbrowser
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # To enable Cross-Origin Resource Sharing (CORS) if necessary
import joblib
import time
import threading

# Initialize Flask app
app = Flask(__name__)

# Enabling CORS if you are working with a frontend and backend on different ports
CORS(app)

# Load the trained model and vectorizer
model = joblib.load('multi_output_model.pkl')
vectorizer = joblib.load('symptom_vectorizer.pkl')

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

# Define the prediction function
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symptom_input = data.get('symptom')

    if not symptom_input:
        return jsonify({'error': 'Symptom is required'}), 400

    # Transform the input symptom using the vectorizer
    symptom_vector = vectorizer.transform([symptom_input])

    # Get predictions from the model
    predictions = model.predict(symptom_vector)

    # Return predictions in a dictionary format
    response = {
        'Tests': predictions[0][0],
        'Medicines': predictions[0][1],
        'Dosages': predictions[0][2],
        'Suggestions': predictions[0][3]
    }

    return jsonify(response)

def open_browser():
    time.sleep(1)  # Give the server a moment to start
    webbrowser.open('http://127.0.0.1:5000/')  # Open the Flask app's URL

if __name__ == '__main__':
    # Start the Flask server in a background thread
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()
    
    # Open the browser in a separate thread
    open_browser()
