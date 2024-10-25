import pickle
from sklearn.dummy import DummyClassifier

# Create a dummy classifier (it will just predict the most frequent class)
model = DummyClassifier(strategy="most_frequent")

# Fit the dummy model on some fake data
X = [[7, 20, 3, 15, 10, 5]]  # Sample data with pH, temperature, etc.
y = [1]  # Sample output (quality class)
model.fit(X, y)

# Save the model to a file
with open('water_quality_model.pkl', 'wb') as f:
    pickle.dump(model, f)
