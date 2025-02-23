import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Ensure correct file path and name

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Print column names to verify correctness
print("Column Names:", df.columns.tolist())

# Identify the correct column name for cuisines
cuisine_column = 'Cuisines'  # Adjust if the column name is different

# Check if the column exists
if cuisine_column in df.columns:
    # Count occurrences of each cuisine
    cuisine_counts = df[cuisine_column].value_counts()
    
    # Get total restaurants count
    total_restaurants = len(df)
    
    # Get the top 3 cuisines
    top_cuisines = cuisine_counts.head(3)
    
    # Calculate percentage
    top_cuisine_percentages = (top_cuisines / total_restaurants) * 100
    
    # Print results
    print("\nTop 3 Cuisines with Percentages:")
    print(top_cuisine_percentages)
else:
    print(f"Error: Column '{cuisine_column}' not found in the dataset.")
