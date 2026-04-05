from flask import Flask, jsonify
from config.ollama import init_ollama
from routes import main_router

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50MB

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "Server is running"}), 200

for blueprint in main_router:
    app.register_blueprint(blueprint, url_prefix="/api")

if __name__ == "__main__":
    init_ollama()
    app.run(host="0.0.0.0", port=3000)
