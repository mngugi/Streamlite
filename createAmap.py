import folium
from IPython.display import display, IFrame

# Center coordinates for the map
map_center = [40.7128, -74.0060]

# Create a map centered at the specified coordinates
map_loc = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
folium.Marker([40.7128, -74.0060],
              popup="New York",
              icon=folium.Icon(color="blue", icon="info-sign")).add_to(map_loc)

# Save the map to an HTML file
map_loc.save("map.html")

# Display the map in an IFrame
display(IFrame("map.html", width=700, height=500))
