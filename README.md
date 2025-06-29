
# 🥔 Potato Disease Classification

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)](https://www.tensorflow.org/)
[![React](https://img.shields.io/badge/Frontend-React-blue?logo=react)](https://reactjs.org/)
[![Docker](https://img.shields.io/badge/Docker-enabled-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A full-stack potato disease classification system using CNN, TensorFlow Serving, FastAPI, and React — built as a follow-along learning project.

---

## 📌 Overview

This system classifies potato leaf images into:
- **Early Blight**
- **Late Blight**
- **Healthy**

It includes:
- A CNN model trained using TensorFlow
- Model served using **TensorFlow Serving + Docker**
- A **FastAPI** backend (optional) that communicates with the serving endpoint
- A **React** frontend for user interaction

---

## 📁 Project Structure

```

PotatoDisease\_Classification/
├── api/                      # Optional FastAPI backend
├── frontend/                 # React frontend
├── models/
│   └── potato\_model/
│       └── 1/                # TensorFlow SavedModel format
│           ├── saved\_model.pb
│           └── variables/
├── models.config             # TensorFlow Serving config file
├── training/                 # Model training notebooks/scripts
├── main.py                   # Entry file for FastAPI (run in PyCharm if needed)
└── README.md

````

---

## 🧠 Model Training

Model training is done using scripts or notebooks in the `training/` directory. The final model is exported using:

```python
tf.saved_model.save(model, "models/potato_model/1")
````

Ensure your `models.config` file looks like this:

```text
model_config_list: {
  config: {
    name: 'potato_model',
    base_path: '/models/potato_model',
    model_platform: 'tensorflow'
  }
}
```

---

## 🐳 Running TensorFlow Serving via Docker

Make sure you have **Docker Desktop running**. Then run the following in **PowerShell**:

```bash
docker run -t --rm -p 8501:8501 `
  -v "yourFilePath\models:/models" `
  tensorflow/serving `
  --model_config_file=/models/models.config
```

This hosts your model at:
`http://localhost:8501/v1/models/potato_model:predict`

You can send POST requests with image data for inference from:

* The frontend
* A Python script
* Postman/cURL

---

## 📦 Frontend (React)

1. Navigate to `frontend/`

```bash
cd frontend
```

2. Install and run:

```bash
npm install
npm start
```

Frontend will be served at [http://localhost:3000](http://localhost:3000)

---

## 📡 Sending Prediction Requests

If using Python:

```python
import requests
import numpy as np

url = "http://localhost:8501/v1/models/potato_model:predict"

# Example input (must match your model input shape)
data = {"instances": [[[...], [...], ...]]}

response = requests.post(url, json=data)
print(response.json())
```

If using FastAPI (optional), you can call this TF Serving endpoint inside your API routes.

---

## 🧰 Tools & Tech Stack

* TensorFlow 2.x
* TensorFlow Serving (Docker)
* React
* FastAPI (optional)
* PyCharm for development
* Windows PowerShell for Docker execution

---

## ✍️ Author

**Noopur Holmes**
🔗 [GitHub](https://github.com/noopur1811)

---

## 🪪 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


