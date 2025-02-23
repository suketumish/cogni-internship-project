import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant columns
lat_column = 'Latitude'
long_column = 'Longitude'

# Drop missing values
df = df.dropna(subset=[lat_column, long_column])

# Apply K-Means clustering
num_clusters = 5  # Adjust based on your dataset
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[[long_column, lat_column]])

# Plot clusters
plt.figure(figsize=(10, 6))
plt.scatter(df[long_column], df[lat_column], c=df['Cluster'], cmap='rainbow', alpha=0.6, edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black', marker='X', s=200, label="Centroids")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Clusters")
plt.legend()
plt.show()
