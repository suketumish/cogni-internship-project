import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
price_column = 'Price range'  # Ensure this column exists in your dataset

# Count occurrences of each price range
price_counts = df[price_column].value_counts().sort_index()

# Plot the distribution as a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=price_counts.index, y=price_counts.values, palette="viridis")

# Add labels and title
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Price Ranges Among Restaurants")
plt.xticks(rotation=0)  # Ensure labels are readable
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
