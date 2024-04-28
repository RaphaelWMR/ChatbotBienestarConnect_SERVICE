# pip install flask python-dotenv google-generativeai
from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
import socket
from dotenv import load_dotenv

# DOTENV
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Lee el archivo que contiene las instrucciones
def read_instruction_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Servidor Flask
app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.form["user_input"]
        print(f"User: {user_input}")
        response = chat.send_message(instruction + user_input)
        print(f"Bot: {response.text}")
        return jsonify({"response": response.text})

    except Exception as e:
        print(f"Bot: {e}")
        return jsonify(
            {"response": "¿Podrias volver a formular tu pregunta?, no entendí bien"}
        )

# Cargando el chatbot
genai.configure(api_key=API_KEY)  # Crear un archivo .env y poner API_KEY="la key"
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
instruction = read_instruction_from_file("knowledge.txt")

# Main
if __name__ == "__main__":
    # app.run(host='0.0.0.0'debug=True)
    ip_address = socket.gethostbyname(socket.gethostname())
    _port = os.getenv('PORT','5001')
    _host = os.getenv('HOST','0.0.0.0') 
    app.run(debug=False, host=_host, port=_port)
    print(f"Servidor flask corriendo en http://{ip_address}:{_port}")