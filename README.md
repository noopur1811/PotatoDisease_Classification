
```markdown
# 🥔 Potato Disease Classification

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)](https://www.tensorflow.org/)
[![React](https://img.shields.io/badge/Frontend-React-blue?logo=react)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A full-stack potato disease classification system built using CNN, FastAPI, and React — developed as a follow-along project to learn end-to-end ML deployment.

---

## 📌 Overview

This project detects diseases in potato plant leaves using a Convolutional Neural Network (CNN). It supports classification into three categories:
- **Early Blight**
- **Late Blight**
- **Healthy**

The system is composed of:
- A TensorFlow-trained model
- A FastAPI backend to serve predictions
- A React-based frontend for user interaction

---

## 📁 Directory Structure

```

PotatoDisease\_Classification/
├── api/           # FastAPI backend
├── frontend/      # React frontend UI
├── models/        # Saved model (.h5 or TensorFlow format)
├── training/      # Jupyter notebooks for model training
├── .idea/
├── .ipynb\_checkpoints/
└── README.md

````

---

## 🚀 Getting Started

### 🧠 Model Training

Model training is performed using Jupyter notebooks in the `training/` folder. The trained model is exported to the `models/` directory.

> Dataset used: [PlantVillage Potato Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)

### ⚙️ Backend Setup (FastAPI)

1. Navigate to the API folder:

```bash
cd api
````

2. Install dependencies:

```bash
pip install fastapi uvicorn tensorflow pillow python-multipart
```

3. Start the server:

```bash
uvicorn main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 🖥️ Frontend Setup (React)

1. Navigate to the React frontend:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend:

```bash
npm start
```

Runs at [http://localhost:3000](http://localhost:3000) and connects to the FastAPI backend.

---

## 🔌 API Endpoint

* **POST** `/predict`
  Accepts: image file
  Returns: predicted class as JSON

Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -F "file=@sample_leaf.jpg"
```

---

## 📦 Tech Stack

* **Frontend**: React, Axios
* **Backend**: FastAPI, Uvicorn
* **Modeling**: TensorFlow/Keras
* **Data**: PlantVillage Potato Dataset

---

## 📚 Learnings

This project was done as a **follow-along learning experience** to understand:

* Training and saving CNN models
* Serving ML models via APIs
* Building a React frontend and connecting it to a Python backend
* Handling image uploads and predictions end-to-end

---

## ✍️ Author

**Noopur Karkare**
🔗 [GitHub](https://github.com/noopur1811)

---

## 🪪 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

```


