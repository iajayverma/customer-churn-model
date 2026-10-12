# Train a simple churn model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
import joblib
import os

os.makedirs('../models', exist_ok=True)
df = pd.read_csv('../data/churn_sample.csv')
X = df[['tenure','monthly_charges','contract','partner']]
y = df['churn'].map({'Yes':1,'No':0})
X = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)
joblib.dump(clf, '../models/churn_model.pkl')
print('Model trained. Test accuracy:', acc)
