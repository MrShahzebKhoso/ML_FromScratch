
# LightML

LightML is a **from-scratch Machine Learning library** built using Python and NumPy.  
It includes core components used in ML: activation functions, optimizers, probability distributions, metrics, distances, and simple classifiers.  
This project is part of a continuous effort to build an educational, transparent ML toolkit without relying on high‑level frameworks.

---

## 📦 Project Structure

```
LightML/
│
├── lightml/
│   ├── __init__.py
│   │
│   ├── activations/
│   │   ├── __init__.py
│   │   ├── relu.py
│   │   ├── leaky_relu.py
│   │   ├── tanh.py
│   │   ├── sigmoid.py
│   │   ├── softmax.py
│   │   ├── gelu.py
│   │
│   ├── optimizers/
│   │   ├── __init__.py
│   │   ├── gradient_descent.py
│   │   ├── adam.py
│   │   ├── adamw.py
│   │   ├── rmsprop.py
│   │   ├── adagrad.py
│   │   ├── adadelta.py
│   │   ├── nag.py
│   │   ├── nadam.py
│   │
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── f1.py
│   │   ├── r2.py
│   │   └── loss.py
│   │
│   ├── distance/
│   │   ├── __init__.py
│   │   ├── euclidean.py
│   │   ├── manhattan.py
│   │   └── cosine.py
│   │
│   ├── probability/
│   │   ├── __init__.py
│   │   ├── bernoulli.py
│   │   ├── binomial.py
│   │   └── geometric.py
│   │
│   ├── statistics/
│   │   ├── __init__.py
│   │   ├── mean_median_mode.py
│   │   ├── variance_std.py
│   │   ├── percentiles.py
│   │   ├── normalization.py
│   │   └── entropy.py
│   │
│   └── classifiers/
│       ├── __init__.py
│       └── majority.py
│
├── setup.py
├── setup.cfg
├── requirements.txt
└── README.md
```

---

## 🚀 Features

### **📐 Activation Functions**
- ReLU  
- Leaky ReLU  
- Sigmoid  
- Tanh  
- Softmax  
- GELU  

### **🧮 Optimizers**
- Gradient Descent  
- Momentum / NAG  
- RMSProp  
- Adam  
- AdamW  
- Nadam  
- AdaGrad  
- AdaDelta  

### **📊 Metrics**
- F1 Score  
- R² Score  
- Cross-entropy Loss  
- MSE / MAE  

### **📏 Distance Measures**
- Euclidean  
- Manhattan  
- Cosine Similarity  

### **🎲 Probability Distributions**
- Bernoulli  
- Binomial  
- Geometric  

### **📈 Statistics**
- Mean, Median, Mode  
- Variance & Standard Deviation  
- Percentiles  
- Min-max & Z-score Normalization  
- Entropy  

### **🟢 Simple Classifiers**
- Majority Classifier (baseline)

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/MrShahzebKhoso/ML_FromScratch.git
cd ML_FromScratch
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install package locally:

```bash
pip install .
```

---

## 🧪 Usage Examples

### **Example 1 — Using an Activation Function**
```python
import numpy as np
from lightml.activations.sigmoid import sigmoid
from lightml.activations.relu import relu

x = np.array([-2, -1, 0, 1, 2])
x_sigmoid = sigmoid(x)
x_relu = relu(x)
print(f"Sigmoid: {x_sigmoid}")
print(f"ReLU:{x_relu}")

```



### **Example 2 — F1 Micro**
```python
import numpy as np
from lightml.metrics.f1_micro import f1_micro

y_true = np.array([1,0,1,1])
y_pred = np.array([1,1,1,0])
f1_score = f1_micro(y_true, y_pred)
print(f"Micro F1: {f1_score}")

```

---

## 📌 Roadmap (Upcoming)
- Neural network layers (Dense, Dropout)  
- Model training loop  
- Regression & classification models  
- Dataset utilities  
- Documentation website  

---

## 🤝 Contributing
Contributions are welcome!  
Submit issues, feature requests, or pull requests.

---

## 📜 License
MIT License

---

## ⭐ Support
If you like this project, please ⭐ star the repo!
