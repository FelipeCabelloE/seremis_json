from OSMPythonTools.nominatim import Nominatim
import time  # Good practice to add a small delay between requests

# Your list of addresses in Chile
chile_addresses = [
    "Av. Libertador Bernardo O'Higgins 340, Santiago",  # Palacio de La Moneda
    "Calle Prat 875, Valparaíso",  # Edificio Armada de Chile
    "Pasaje Nueva Uno 123, Concepción",  # Example address
    "Calle Anibal Pinto 322, Temuco",
    "Calle Bulnes 90, Puerto Montt",
    "Plaza de Armas, La Serena",  # A well-known landmark
    "Avenida Arturo Prat 220, Iquique",
    "This is not a real address, Chile",  # Example of an address that might not be found
    "Avenida República de Chile 1, Punta Arenas",  # Example in the south
]

# Initialize the Nominatim geocoding service
nominatim = Nominatim()

# List to store results
geocoded_locations = []

print("Starting geocoding process...")

# Loop through each address and query Nominatim
for i, address in enumerate(chile_addresses):
    # Construct the query string - it's good to add "Chile" to help Nominatim
    query_string = f"{address}, Chile"

    print(f"[{i + 1}/{len(chile_addresses)}] Querying: {query_string}")

    try:
        # Query Nominatim
        # The query method returns a list of potential matches (ordered by confidence)
        response = nominatim.query(query_string)

        if response:
            # Get the most likely result (the first one in the list)
            first_result = response[0]

            # Extract latitude and longitude
            lat = first_result.lat()
            lon = first_result.lon()
            display_name = (
                first_result.displayName()
            )  # Optional: get the name Nominatim matched

            print(f"  Found: Latitude={lat}, Longitude={lon}")
            print(f"  Matched: {display_name}")

            geocoded_locations.append(
                {
                    "original_address": address,
                    "latitude": lat,
                    "longitude": lon,
                    "matched_name": display_name,
                }
            )
        else:
            # No results found for this address
            print("  Not found.")
            geocoded_locations.append(
                {
                    "original_address": address,
                    "latitude": None,
                    "longitude": None,
                    "matched_name": None,
                }
            )

    except Exception as e:
        # Handle potential errors (e.g., network issues)
        print(f"  Error querying {query_string}: {e}")
        geocoded_locations.append(
            {
                "original_address": address,
                "latitude": None,
                "longitude": None,
                "matched_name": f"Error: {e}",
            }
        )

    # Add a small delay to avoid hitting Nominatim rate limits too quickly
    # Nominatim's usage policy suggests no heavy usage and max 1 request per second.
    time.sleep(1)

print("\n--- Geocoding Complete ---")
print("Results:")

# Print the collected results
for result in geocoded_locations:
    print(f"Original: {result['original_address']}")
    if result["latitude"] is not None:
        print(f"  Location: ({result['latitude']}, {result['longitude']})")
        print(f"  Matched: {result['matched_name']}")
    else:
        print(
            f"  Location: Not Found ({result.get('matched_name', 'Unknown reason')})"
        )  # Use get for error handling
    print("-" * 20)

# You can further process geocoded_locations (e.g., save to CSV, use in mapping libraries)
