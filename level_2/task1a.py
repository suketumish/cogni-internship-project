import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
rating_column = 'Aggregate rating'  # Ensure this column exists in your dataset

# Plot the distribution as a histogram
plt.figure(figsize=(8, 5))
sns.histplot(df[rating_column], bins=10, kde=True, color="blue")

# Add labels and title
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Ratings")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()

# Determine the most common rating range
most_common_rating_range = df[rating_column].round(1).mode()[0]
print(f"The most common rating range is around {most_common_rating_range}.")
