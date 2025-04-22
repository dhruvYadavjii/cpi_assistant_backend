
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API Key as an environment variable or directly in code
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-REPLACE_THIS")

@app.route("/gpt", methods=["POST"])
def handle_error():
    data = request.get_json()
    error_text = data.get("error", "")
    prompt = f"Analyze this SAP CPI iFlow error and suggest a fix with code or configuration snippet: {error_text}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SAP CPI iFlow expert."},
                {"role": "user", "content": prompt}
            ]
        )
        suggestion = response['choices'][0]['message']['content']
        return jsonify({"reply": suggestion})
    except Exception as e:
        return jsonify({"reply": f"Failed to fetch suggestion: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
