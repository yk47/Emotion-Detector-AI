# 🤖 Emotion Detector AI Web App

An AI-powered web application that detects emotions from user input text. Built using **Flask** and a **Hugging Face Transformer model**, this app analyzes text and identifies emotions like joy, sadness, anger, fear, and more — all through a clean and interactive UI.

---

## 🚀 Features

* 🧠 Real-time emotion detection using NLP
* 🎯 Detects multiple emotions (joy, sadness, anger, fear, disgust, surprise)
* 🌐 Flask-based backend API
* 🎨 Modern responsive frontend with emojis & visual emotion bars
* ⚡ Fast and lightweight (CPU-based, no GPU required)
* ❌ No API key or credit card required

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI Model:** Hugging Face Transformers
* **Frontend:** HTML, CSS, JavaScript
* **ML Framework:** PyTorch (CPU version)

---

## 📂 Project Structure

```
emotion-app/
│
├── app.py
├── emotion_detector.py
├── formatter.py
├── test_emotion.py
├── requirements.txt
├── templates/
│   └── index.html
└── __init__.py
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector
```

### 2️⃣ Install dependencies

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

---

## 🌐 Usage

Open your browser and go to:

```
http://127.0.0.1:8080
```

### Example Input:

```
I feel amazing and happy today!
```

### Example Output:

```
Dominant Emotion: joy 😄
```

---

## 🔌 API Endpoint

### POST `/emotion`

#### Request:

```json
{
  "text": "I am feeling great today!"
}
```

#### Response:

```json
{
  "emotions": {
    "joy": 0.92,
    "sadness": 0.01,
    "anger": 0.01,
    "fear": 0.03,
    "disgust": 0.03
  },
  "dominant_emotion": "joy"
}
```

---

## 🧪 Running Tests

```bash
python -m unittest
```

---

## ⚠️ Notes

* First run will download the AI model (~100MB)
* Works offline after initial setup
* Uses CPU-only PyTorch for compatibility

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Yash Karnik**
Cybersecurity Enthusiast | AI Developer | Flutter Developer

---
