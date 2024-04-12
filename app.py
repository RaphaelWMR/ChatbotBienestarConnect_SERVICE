# pip install flask python-dotenv google-generativeai
from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
import socket

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY) # Crear un archivo .env y poner API_KEY="la key"

app = Flask(__name__)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def read_instruction_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

instruction = read_instruction_from_file("knowledge.txt")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    response = chat.send_message(instruction + user_input)
    return jsonify({"response": response.text})


if __name__ == "__main__":
    # app.run(host='0.0.0.0'debug=True)
    ip_address = socket.gethostbyname(socket.gethostname())
    app.run(debug=True, host=ip_address)
    print(f"Flask server running at http://{ip_address}:5000")
