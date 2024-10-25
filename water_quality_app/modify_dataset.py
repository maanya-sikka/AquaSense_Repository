import pandas as pd

# Load the dataset
df = pd.read_csv('hack_water.csv')

# Check if the 'result' column exists, if not, create it with default values (Safe)
if 'result' not in df.columns:
    df['result'] = 'Safe'  # Default all rows to 'Safe'

# Define a function to classify water quality based on multiple features
def classify_result(row):
    # If the result is already manually set as 'Unsafe', keep it as 'Unsafe'
    if row['result'] == 'Unsafe':
        return 'Unsafe'
    
    # Classify based on pH, Dissolved Oxygen, Turbidity, and Conductivity
    if (6.5 <= row['pH'] <= 8.5) and (row['Dissolved_Oxygen_mgL'] > 6) and (row['Turbidity_NTU'] < 5) and (row['Conductivity_uScm'] < 500):
        return 'Safe'
    else:
        return 'Unsafe'

# Apply the function to the dataset
df['result'] = df.apply(classify_result, axis=1)

# Save the modified dataset
df.to_csv('hack_water_modified.csv', index=False)

print("Dataset modified and saved as hack_water_modified.csv")
