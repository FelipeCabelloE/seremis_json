import json
from pydantic_code.jsonseremis_model import Seremi


from typing import List, Optional
from pydantic import BaseModel, ValidationError, parse_obj_as


def open_jsonseremis(filename: str):
    # --- Load JSON data from the file ---
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        print(f"Successfully loaded data from {filename}")

        # --- Parse the list of dictionaries using Pydantic ---
        # We tell Pydantic to parse the entire list into a list of Seremi models.
        print("Parsing data with Pydantic...")
        parsed_seremis: List[Seremi] = parse_obj_as(List[Seremi], raw_data)

        print("Successfully parsed data with Pydantic.")

        # --- You can now work with the validated Pydantic objects ---
        print(f"\nNumber of Seremi entries parsed: {len(parsed_seremis)}")

        return parsed_seremis

        # # Example: Print details of the first entry
        # if parsed_seremis:
        #     first_seremi = parsed_seremis[0]
        #     print("\nFirst entry details:")
        #     print(f"  Region: {first_seremi.Region}")
        #     print(f"  Address: {first_seremi.Address}")
        #     print(f"  Phones: {first_seremi.Phones}")
        #     print(f"  Email: {first_seremi.Email}")
        #     print(f"  Hours: {first_seremi.Hours}")
        #     # Additional_Hours will be None for this entry

        # # Example: Print details of the last entry (which has Additional_Hours)
        # if len(parsed_seremis) > 1:
        #      last_seremi = parsed_seremis[-1]
        #      print("\nLast entry details (Magallanes):")
        #      print(f"  Region: {last_seremi.Region}")
        #      print(f"  Address: {last_seremi.Address}")
        #      print(f"  Phones: {last_seremi.Phones}")
        #      print(f"  Email: {last_seremi.Email}")
        #      print(f"  Hours: {last_seremi.Hours}")
        #      print(f"  Additional Hours: {last_seremi.Additional_Hours}")

    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
    except ValidationError as e:
        print("Pydantic Validation Error:")
        # Pydantic provides detailed errors about what went wrong
        print(e)
    except FileNotFoundError:
        # This case should ideally not happen if file writing was successful,
        # but good to include for robustness.
        print(f"Error: File '{filename}' not found after writing.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
