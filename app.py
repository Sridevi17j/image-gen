from flask import Flask, request, jsonify, render_template, Response
import fal_client
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Ensure FAL_KEY is set
#if 'FAL_KEY' not in os.environ:
#    raise ValueError("FAL_KEY environment variable is not set. Please set it and try again.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Use fal_client.submit instead of fal_client.run
        result = fal_client.submit(
            "fal-ai/flux-pro",
            arguments={
                "prompt": prompt
            },
        ).get()  # This will wait for the result

        # Return the result directly
        return result
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500    
if __name__ == '__main__':
    app.run(debug=True)
