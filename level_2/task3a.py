import pandas as pd
import folium

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant columns
lat_column = 'Latitude'
long_column = 'Longitude'

# Create a base map centered at an average location
map_center = [df[lat_column].mean(), df[long_column].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add markers for each restaurant
for _, row in df.iterrows():
    folium.Marker(
        location=[row[lat_column], row[long_column]],
        popup=row.get('Restaurant Name', 'Unknown Restaurant'),  
        icon=folium.Icon(color="blue", icon="cutlery", prefix="fa")
    ).add_to(restaurant_map)

# Save and display the map
restaurant_map.save("restaurant_locations.html")
print("Map saved as 'restaurant_locations.html'. Open it in a browser to view.")
