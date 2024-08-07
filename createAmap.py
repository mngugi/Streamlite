import folium
from IPython.display import display

map_center = [40.7128, +74.0068]

map_loc = folium.Map(location=map_center, zoom_start=12)


folium.Marker( [40.7128, +74.0060],
               popup="New York",
               icon=folium.Icon(color="blue", icon="info-sign")).add_to(map_loc)

display(map_loc._repr_html_())



