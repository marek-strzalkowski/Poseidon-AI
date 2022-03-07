import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Get data for Machine Learning

data = pd.read_csv('data/combined_data.csv', sep=',')

X = data.drop(columns=['zgon'])
y = data['zgon']

# Create and save A.I. model

model = LogisticRegression(max_iter=1000)
model.fit(X.values,y.values)

with open('data/ai_logistic_regression.pkl','wb') as f:
    pickle.dump(model, f)

# Test A.I. model accuracy

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

test_model = LogisticRegression(max_iter=1000)
test_model.fit(X_train, y_train)
predictions = test_model.predict(X_test)
score = accuracy_score(y_test, predictions)

print(score)