import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Load the dataset (adjust this part based on the location of your CSV)
data = pd.read_csv('iris_dataset.csv')
# Check the column names
print(data.columns)
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('species', axis=1), data['species'],
test_size=0.3, random_state=42)
# Initialize the SVM classifier
svm = SVC(kernel='linear')
# Train the model
svm.fit(X_train, y_train)
# Make predictions
y_pred = svm.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of the SVM model: {accuracy:.2f}')
# Train an SVM model with a polynomial kernel
svm_poly = SVC(kernel='poly', degree=3)
svm_poly.fit(X_train, y_train)
# Predict the test set labels
y_pred = svm_poly.predict(X_test)
# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Polynomial SVM accuracy: {accuracy:.2f}')
# Train an SVM model with an RBF kernel
svm_rbf = SVC(kernel='rbf')
svm_rbf.fit(X_train, y_train)
# Predict the test set labels
y_pred = svm_rbf.predict(X_test)
# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'RBF SVM accuracy: {accuracy:.2f}')
