from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

# Specify the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the maximum allowed file size (in bytes)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/run_inference', methods=['POST'])
def run_inference():
    try:
        # Check if the POST request contains the 'file' key
        if 'file' not in request.files or 'selection' not in request.form:
            return jsonify({'error': 'Missing file or gender parameter in the request'}), 400
        
        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save the uploaded file to the upload folder
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Get the height from the request
        height = request.form.get('height')
        sex = request.form.get('selection')

        # Validate height (numeric, positive integer, within a reasonable range)

        # Construct the command
        command = f'python inference.py -i "{file_path}" -ht {height} -g {sex}'

        # Run the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Return the output
            response = {'output': result.stdout}

            # Delete the uploaded file from the server after processing
            os.remove(file_path)

            return jsonify(response)
        else:
            # Return an error response
            return jsonify({'error': 'Failed to run inference script'}), 500
    except Exception as e:
        # Log the exception
        app.logger.error(f'Error processing request: {str(e)}')

        # Return an error response
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
