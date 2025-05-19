from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Seremis_app")

location = geolocator.geocode("Palacio la Moneda")

print(location.address)
