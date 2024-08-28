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
async def generate_image():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        result = fal_client.submit(
            "fal-ai/flux-pro",
            arguments={
                "prompt": prompt
            },
        ).get()
        time.sleep(10)

        # Assume the result is the image in binary format or base64
        return jsonify(result)

        #if result:
            # Assuming result is a dictionary with image information
         #   return jsonify(result)
        else:
            return jsonify({'error': 'No image generated'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
