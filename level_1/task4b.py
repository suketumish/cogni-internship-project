import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant columns
online_delivery_column = 'Has Online delivery'
rating_column = 'Aggregate rating'

# Convert the "Has Online delivery" column to lowercase for consistency
df[online_delivery_column] = df[online_delivery_column].astype(str).str.lower()

# Calculate average ratings
avg_rating_with_delivery = df[df[online_delivery_column] == 'yes'][rating_column].mean()
avg_rating_without_delivery = df[df[online_delivery_column] == 'no'][rating_column].mean()

# Print results
print(f"Average rating of restaurants WITH online delivery: {avg_rating_with_delivery:.2f}")
print(f"Average rating of restaurants WITHOUT online delivery: {avg_rating_without_delivery:.2f}")
