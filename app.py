from geopy.geocoders import Nominatim

def get_lat_lon(address):
    # Initialize the Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Geocode the address
    location = geolocator.geocode(address)

    # Check if the location is found
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example usage
address = "C San Jaime 11, Otivar, Granada"
latitude, longitude = get_lat_lon(address)

if latitude and longitude:
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Address not found.")
