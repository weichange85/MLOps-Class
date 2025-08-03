from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a small, fast text generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        data = request.get_json(force=True) if request.is_json else request.form
        prompt = data.get("prompt", "")
        
        if not prompt:
            return jsonify({"error": "Missing 'prompt' field"}), 400

        result = generator(prompt, max_length=50, num_return_sequences=1)
        return jsonify({"generated_text": result[0]['generated_text']})
    
    return '''
        <form method="post">
            <label>Enter your prompt:</label><br>
            <textarea name="prompt" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Generate Text">
        </form>
    '''

@app.route('/', methods=['GET'])
def home():
    return "Text Generator API is up!"

if __name__ == '__main__':
    app.run(debug=True)
