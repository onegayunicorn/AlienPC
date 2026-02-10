from flask import Flask, jsonify, request
from genomics.src.synthetic_base_detection.detector import detect
import yaml
from pathlib import Path

app = Flask(__name__)

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
    return jsonify({"service": "AlienPC Genomics Engine", "version": "0.1.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=CONFIG.get("port", 5000))
