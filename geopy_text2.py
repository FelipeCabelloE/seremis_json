from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Seremis_app")

location = geolocator.geocode("Seremi Bienes Nacionales Antofagasta")


if __name__ == "__main__":
    print(location.address)

    print((location.latitude, location.longitude))

    print(location.raw)
