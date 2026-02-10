from flask import Flask, jsonify, request
from genomics.src.synthetic_base_detection.detector import detect
from genomics.src.api.claude_assistant import claude_bp
import yaml
from pathlib import Path

app = Flask(__name__)

# Register Claude AI Blueprint
app.register_blueprint(claude_bp)

# Load configuration
CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "api_config.yaml"
if CONFIG_PATH.exists():
    CONFIG = yaml.safe_load(CONFIG_PATH.read_text())
else:
    CONFIG = {"port": 5000}

@app.route("/detect/synthetic", methods=["POST"])
def detect_synthetic():
    seq = request.json.get("sequence", "")
    return jsonify(detect(seq))

@app.route("/status")
def status():
    return jsonify({
        "service": "AlienPC Genomics Engine",
        "version": "1.0.1",
        "features": ["synthetic_base_detection", "claude_ai_assistant"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=CONFIG.get("port", 5000))
