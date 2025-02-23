import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Count occurrences of each restaurant name (to find chains)
restaurant_counts = df['Restaurant Name'].value_counts()

# Filter for restaurant chains (restaurants appearing more than once)
restaurant_chains = restaurant_counts[restaurant_counts > 1].index

# Filter dataset for only chain restaurants
df_chains = df[df['Restaurant Name'].isin(restaurant_chains)]

# Group by restaurant name to calculate average rating & total votes
chain_analysis = df_chains.groupby('Restaurant Name').agg(
    Avg_Rating=('Aggregate rating', 'mean'),
    Total_Votes=('Votes', 'sum'),
    Locations=('Restaurant Name', 'count')  # Number of locations
).reset_index()

# Sort by highest average rating
top_rated_chains = chain_analysis.sort_values(by='Avg_Rating', ascending=False)

# Sort by most popular (highest total votes)
most_popular_chains = chain_analysis.sort_values(by='Total_Votes', ascending=False)

# Display results
print("Top 10 Highest Rated Chains:")
print(top_rated_chains.head(10))

print("\nTop 10 Most Popular Chains (by Votes):")
print(most_popular_chains.head(10))
