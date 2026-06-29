import os
import base64
from flask import Flask, request, jsonify, send_from_directory
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static")

VISION_KEY = os.environ.get("VISION_KEY", "")
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT", "").rstrip("/")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if not VISION_KEY or not VISION_ENDPOINT:
        return jsonify({"error": "Missing Azure credentials"}), 500

    data = request.get_json(silent=True) or {}
    image_url = data.get("url")
    image_base64 = data.get("image_base64")

    # ✅ FIXED Azure endpoint (NO features parameter)
    api_url = (
    f"{VISION_ENDPOINT}/computervision/imageanalysis:analyze"
    f"?api-version=2023-10-01"
    f"&features=tags,read"
)
    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY
    }

    try:
        if image_url:
            headers["Content-Type"] = "application/json"
            resp = requests.post(api_url, headers=headers, json={"url": image_url}, timeout=20)

        elif image_base64:
            if "," in image_base64:
                image_base64 = image_base64.split(",", 1)[1]

            image_bytes = base64.b64decode(image_base64)
            headers["Content-Type"] = "application/octet-stream"

            resp = requests.post(api_url, headers=headers, data=image_bytes, timeout=20)

        else:
            return jsonify({"error": "No image provided"}), 400

    except requests.RequestException as exc:
        return jsonify({"error": str(exc)}), 502

    try:
        body = resp.json()
    except ValueError:
        return jsonify({"error": "Invalid Azure response", "raw": resp.text}), 500

    # ---------------- BRAND DETECTION ----------------
    brand_keywords = [
        "nike", "adidas", "puma", "apple", "samsung",
        "hp", "lenovo", "dell", "sony", "canon",
        "lg", "bosch", "tesla", "honda", "toyota"
    ]

    detected_brand = "Unknown"

    # Extract tags safely
    tags = []
    try:
        tags = [
            t.get("name", "").lower()
            for t in body.get("tagsResult", {}).get("values", [])
        ]
    except:
        pass

    # Extract OCR safely
    ocr_text = ""
    try:
        read = body.get("readResult", {})
        blocks = read.get("blocks", [])
        for b in blocks:
            for line in b.get("lines", []):
                ocr_text += line.get("text", "").lower() + " "
    except:
        pass

    combined = " ".join(tags) + " " + ocr_text

    for b in brand_keywords:
        if b in combined:
            detected_brand = b.upper()
            break

    body["final_brand"] = detected_brand

    return jsonify(body), resp.status_code


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "configured": bool(VISION_KEY and VISION_ENDPOINT)
    })


if __name__ == "__main__":
    app.run(debug=True)