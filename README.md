
```markdown
# Potato Disease Classification

This project is a deep learning-based image classification system for detecting diseases in potato leaves using Convolutional Neural Networks (CNNs). It classifies images into three categories: **Early Blight**, **Late Blight**, and **Healthy**.

## 📁 Dataset

The dataset is sourced from the [PlantVillage dataset](https://www.kaggle.com/datasets/emmarex/plantdisease), specifically the potato subset. It includes labeled images of:

- Early Blight
- Late Blight
- Healthy Leaves

The dataset is organized into three folders:
```

Potato/
├── Potato\_\_\_Early\_blight/
├── Potato\_\_\_Late\_blight/
└── Potato\_\_\_healthy/

````

## 🚀 Features

- Image preprocessing with TensorFlow/Keras ImageDataGenerator
- CNN architecture for classification
- Training with real-time data augmentation
- Model evaluation using accuracy and loss metrics
- Saved model for future inference

## 🧠 Model Architecture

The CNN model includes:

- Convolutional layers with ReLU activation
- MaxPooling for dimensionality reduction
- Dropout to prevent overfitting
- Dense layers for final classification

## 📊 Training & Evaluation

- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metrics: Accuracy
- Epochs: 50
- Batch Size: 32

## 📦 Requirements

- Python 3.x
- TensorFlow
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
````

## 🖼️ Sample Predictions

The model predicts the class of a given potato leaf image and displays the result:

* `Early Blight`
* `Late Blight`
* `Healthy`

## 🏁 How to Run

1. Clone the repository:

```bash
git clone https://github.com/noopur1811/PotatoDisease_Classification.git
cd PotatoDisease_Classification
```

2. Train the model:

```bash
python train.py
```

3. Run predictions:

```bash
python predict.py
```

## 📈 Results

* Achieved high classification accuracy (>95%)
* Effective disease differentiation on unseen data
* Lightweight and fast inference

## 📚 References

* [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
* TensorFlow & Keras documentation

## 👩‍💻 Author

**Noopur Karkare**
[GitHub](https://github.com/noopur1811)

---
