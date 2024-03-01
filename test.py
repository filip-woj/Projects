import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Nov09JnyExport.csv')

geo = pd.read_csv()


from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="underground station locations")

# Define a function to geocode a location
def geocode_location(location):
    location = geolocator.geocode(location)
    return (location.latitude, location.longitude) if location else (None, None)

# Geocode each start station in the DataFrame
df['Latitude'], df['Longitude'] = zip(*df['StartStn'].apply(geocode_location))
