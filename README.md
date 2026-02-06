# Breast Cancer Prediction using SVM

This project implements a breast cancer classification system using a Support Vector Machine (SVM). 
The model predicts whether a tumor is **malignant (cancer)** or **benign (no cancer)** based on numerical features extracted from cell nuclei images.

## 📌 Dataset
- Wisconsin Breast Cancer Diagnostic Dataset
- 569 samples with 30 numerical features
- Binary classification (Malignant / Benign)

## 🧠 Model
- Algorithm: Support Vector Machine (SVM)
- Kernel: RBF
- Hyperparameter tuning using GridSearchCV
- Accuracy achieved: ~94%

## 🖥️ Application
A simple Python Tkinter-based GUI is provided where users can:
- Enter feature values
- Get real-time cancer prediction

## 📂 Project Structure

## 📂 Project Structure
breast-cancer-prediction
├── train_model.py # Model training and evaluation
├── app.py # GUI application
├── cancer_model.pkl # Trained model



```
## ▶️ How to Run

### 1. Install dependencies

bash pip install numpy pandas scikit-learn joblib

python train_model.py

python app.py

```
⚠️ Disclaimer

This project is for educational and research purposes only and should not be used for real-world medical diagnosis.

👤 Author

Satpal Singh
