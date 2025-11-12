from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = GaussianNB()
model.fit(X_train, y_train)

print("Predictions:", model.predict(X_test))
print("Accuracy:", model.score(X_test, y_test))
