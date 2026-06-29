# AI Brand Detection & Image Analysis

A web application that analyzes images using **Azure AI Vision** and performs **brand detection** based on OCR text and semantic tags. Users can upload an image or provide an image URL, and the application extracts intelligent insights including detected brands, image tags, confidence scores, and text recognition.

The frontend communicates only with a secure **Flask backend**, which stores the Azure AI Vision credentials as environment variables. This ensures that API keys are never exposed in the browser.

---

## Features

* 🖼️ Upload an image from your device
* 🌐 Analyze images using a direct image URL
* 🏷️ Brand Detection (using OCR text and semantic tags)
* 🔍 Semantic Tag Detection
* 📝 Optical Character Recognition (OCR)
* 📊 Confidence Scores for detected tags
* 🔒 Secure server-side Azure API integration
* 💻 Modern Microsoft-inspired responsive user interface

---

## Project Structure

```text
Brand-detection/
├── app.py                  # Flask backend
├── requirements.txt         # Python dependencies
├── .gitignore
├── README.md
└── static/
    └── index.html           # Frontend UI
```

---

## Technology Stack

* Python
* Flask
* Azure AI Vision Image Analysis API
* HTML5
* CSS3
* JavaScript
* REST API
* Git & GitHub

---

## How It Works

```text
Browser
    │
    ▼
Upload Image / Image URL
    │
    ▼
POST /analyze
    │
    ▼
Flask Backend
    │
    ▼
Azure AI Vision API
    │
    ▼
Brand Detection Logic
(OCR + Semantic Tags)
    │
    ▼
Results Returned to Browser
```

The backend securely stores the Azure credentials using environment variables (`VISION_KEY` and `VISION_ENDPOINT`) and performs all communication with Azure AI Vision. The frontend never has direct access to the API keys.

---

## Brand Detection

Unlike Azure AI Vision, which primarily provides image understanding, this project adds a custom brand detection layer.

The application:

1. Sends the image to Azure AI Vision.
2. Extracts semantic tags and OCR text.
3. Searches for known brand keywords.
4. Displays the detected brand if a match is found.

Currently supported brands include:

* Nike
* Adidas
* Puma
* Apple
* Samsung
* HP
* Lenovo
* Dell
* Sony
* Canon
* LG
* Bosch
* Tesla
* Honda
* Toyota

If no matching brand is found, the application displays:

```
No known brand detected
```

---

## Local Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Brand-detection.git
cd Brand-detection
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```text
VISION_KEY=your_azure_key
VISION_ENDPOINT=https://your-resource.cognitiveservices.azure.com
```

Run the application:

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## API Endpoints

### GET /

Loads the web application.

---

### POST /analyze

Accepts either:

```json
{
    "url": "https://example.com/image.jpg"
}
```

or

```json
{
    "image_base64": "..."
}
```

Returns:

* Detected Brand
* Image Tags
* Confidence Scores
* OCR Text
* Azure AI Vision Response

---

### GET /health

Returns:

```json
{
    "status": "ok",
    "configured": true
}
```

---

## Security

* Azure API keys are stored as environment variables.
* The frontend never communicates directly with Azure.
* Sensitive credentials are excluded from Git using `.gitignore`.

---

## Future Improvements

* AI logo detection using YOLO
* Azure Custom Vision integration
* Support for additional brands
* Object detection
* Better logo recognition without OCR
* Deployment using Docker and Azure App Service

---

## Author

**Anwesha Rawat**

This project was developed as a learning project to explore Azure AI Vision, Flask backend development, image analysis, OCR, and custom brand detection.
