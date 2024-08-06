import re


def dms_to_decimal(dms_str):
    # Regular expression to parse the DMS format
    pattern = r'(\d+) deg (\d+)' + "'" + r' (\d+\.\d+)" ([NSEW])'
    match = re.match(pattern, dms_str)

    if not match:
        raise ValueError(f"Invalid DMS string: {dms_str}")

    degrees = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))
    direction = match.group(4)

    # Convert DMS to decimal degrees
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)

    # Adjust the sign based on the direction
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees

    return decimal_degrees


# Define the strings
latitude_str = "39 deg 9' 7.99\" N"
longitude_str = "106 deg 24' 20.73\" W"

# Convert to decimal degrees
latitude_decimal = dms_to_decimal(latitude_str)
longitude_decimal = dms_to_decimal(longitude_str)

# Print the results
print(f"Latitude (decimal degrees): {latitude_decimal}")
print(f"Longitude (decimal degrees): {longitude_decimal}")

# Display the results using Streamlit
import streamlit as st

st.write("### DMS to Decimal Degrees Conversion")
st.write(f"**Latitude:** {latitude_str} -> **{latitude_decimal}**")
st.write(f"**Longitude:** {longitude_str} -> **{longitude_decimal}**")
