import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your file

# Count cuisine occurrences
top_cuisines = df['Cuisines'].value_counts().head(3)




print(top_cuisines)
