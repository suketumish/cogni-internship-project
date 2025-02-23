import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Count occurrences of each restaurant name
restaurant_counts = df['Restaurant Name'].value_counts()

# Filter for restaurant chains (restaurants appearing more than once)
restaurant_chains = restaurant_counts[restaurant_counts > 1]

# Display the top 10 largest chains
print("Top Restaurant Chains:")
print(restaurant_chains.head(10))
