from flask import Flask, jsonify
from num2words import num2words
import json

app = Flask(__name__)

def load_number_from_json(file_path):
    """ Load number from JSON file """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            return config.get('number')
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

@app.route('/data', methods=['GET'])
def get_data():
    """ API to fetch number and return its word representation """
    number = load_number_from_json('config.json')  # Read from JSON file
    if number is None:
        return jsonify({'error': 'No valid number provided in JSON file'}), 400
    try:
        number = int(number)
        words = num2words(number)
        return jsonify({'number': number, 'words': words})
    except ValueError:
        return jsonify({'error': 'Invalid number provided in JSON file'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
