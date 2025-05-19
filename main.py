from pydantic_code.jsonseremis_parser import open_jsonseremis
from functools import partial

from geopy.geocoders import Nominatim, GoogleV3


def main():
    seremis = open_jsonseremis("./seremis.json")
    geolocator = GoogleV3(user_agent="Seremis App")

    geocode = partial(geolocator.geocode, language="es")
    for seremi in seremis:
        print(f"... Searching for seremi in Region: {seremi.Region}")

        location = geocode(seremi.Address + f", {seremi.Region}" + ", Chile")
        print(location)
        print(f"Searching for Address: {seremi.Address}")
        print(location.address)
        print((location.latitude, location.longitude))


if __name__ == "__main__":
    main()
