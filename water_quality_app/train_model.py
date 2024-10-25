import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the modified dataset
df = pd.read_csv('hack_water_modified.csv')

# Prepare the features (input data) and target (output label)
X = df[['pH', 'Temperature_C', 'Turbidity_NTU', 'Dissolved_Oxygen_mgL', 'Conductivity_uScm']]  # Features
y = df['result']  # Target label (Safe/Unsafe)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a file
with open('water_quality_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model retrained and saved as water_quality_model.pkl")
