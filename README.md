# Customer Churn Model

A complete and straightforward machine learning pipeline to predict customer churn using a Random Forest Classifier.

## 🎯 Project Goal

The primary objective of this project is to build a predictive model that can identify customers who are likely to stop using a service (churn). By accurately predicting churn, businesses can proactively take measures to retain valuable customers. This repository demonstrates a full, albeit simple, end-to-end pipeline from training to model serialization.

## ✨ Key Features

- **🧹 Clean, Synthetic Dataset:** Includes a sample `churn_sample.csv` for easy and immediate training.
- **🤖 Model Training:** A clear and commented Python script (`train/train_churn.py`) that handles data loading, training, and saving.
- **🌳 Random Forest Classifier:** Implements a powerful and popular ensemble learning method for robust classification.
- **📦 Model Serialization:** The trained model is saved as `churn_model.pkl`, ready for deployment or inference.
- **📋 Minimal Dependencies:** The `requirements.txt` file makes setup quick and easy.

## 🛠️ Tech Stack

- **Language:** Python
- **Core Libraries:**
 - `scikit-learn` (for the machine learning model)
 - `pandas` (for data manipulation)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation & Usage

1. **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/customer-churn-prediction.git](https://github.com/your-username/customer-churn-prediction.git)
    cd customer-churn-prediction
    ```
 *(Replace `your-username` with your GitHub username)*

2. **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the training script:**
    ```sh
    python train/train_churn.py
    ```

5. **Check the output:**
 After the script finishes, you will find the trained model saved at `models/churn_model.pkl`.

## 📁 Project Structure

## Repository Maintainer

Ajay Verma

## Attribution

This repository is based on an open-source project distributed under its original license. The original work is by the authors of rahuloraj/Customer-Churn-Prediction.

All original copyright notices and the LICENSE file are preserved. This copy adds only repository-level metadata; the source code remains the work of the original authors.
