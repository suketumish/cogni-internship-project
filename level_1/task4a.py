import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
online_delivery_column = 'Has Online delivery'  # Ensure this column exists in your dataset

# Convert column to consistent format (if necessary)
df[online_delivery_column] = df[online_delivery_column].astype(str).str.lower()

# Count occurrences
online_delivery_count = df[online_delivery_column].value_counts()

# Calculate percentage of restaurants that offer online delivery
if 'yes' in online_delivery_count:
    online_delivery_percentage = (online_delivery_count['yes'] / len(df)) * 100
else:
    online_delivery_percentage = 0  # No restaurants offer online delivery

# Print result
print(f"Percentage of restaurants that offer online delivery: {online_delivery_percentage:.2f}%")
