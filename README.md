# Capstone Project - Clinical Recommendation System Using Rando Forest

A full-stack machine learning web application that provides clinical recommendations (Tests, Medicines, Dosages, Suggestions) based on user-input symptoms. Built using Python, Flask, HTML, CSS, JavaScript, and trained with a Random Forest model.


## Features

- Accepts multiple symptoms as input.
- Predicts tests, medicines, dosages, and suggestions using a trained ML model.
- Allows users to manually add/edit recommendations.
- Generates PDF reports from selected suggestions.
- Built-in clear/reset functionality.
- User-friendly frontend with interactive features.


## 💻 Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Machine Learning:** Random Forest Classifier
- **Data Handling:** Pandas, Pickle
- **PDF Generation:** jsPDF


## Installation & Local Setup

### 1. Clone the Repository

git clone https://github.com/mdazharulislamnk/Capstone_Project_Clinical_Recommendation_System_Using_RandomForest.git
cd Capstone_Project_Clinical_Recommendation_System_Using_RandomForest

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

# OR

source venv/bin/activate  # macOS/Linux

### 3. Install Required Packages
pip install -r requirements.txt

### 5. Run the Flask App
python app.py
The server will start at http://127.0.0.1:5000/

## ⚠️ Dataset & Model Information
Important: This repository does not include the training dataset due to privacy/size reasons.

## Pre-trained files used:
multi_output_model.pkl – Random Forest multi-label classifier
symptom_vectorizer.pkl – Vectorizer for symptom transformation



📄 License
This project is for academic and educational use only. Not intended for real-world clinical diagnosis.

👤 Author
Md. Azharul Islam
BSc in CSE, East West University
GitHub: mdazharulislamnk
LinkedIn: mdazharulislam



