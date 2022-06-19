import json
import re


def complex_processor(concatenated_streets: list) -> json:

    """
    Function that reads complex concatenated street list and
    returns street name and number json object
    """
    regex = r"^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$"
    streets = []
    for concatenated_street in concatenated_streets:
        street = re.findall(regex, concatenated_street)
        housenumber = ""
        street_array = []
        for item in street[0]:
            street_array.append(item)

        ordered_street_array = sorted(street_array, key=len, reverse=True)

        for index in range(1, len(ordered_street_array)):
            housenumber = housenumber + ordered_street_array[index]
        streetname = ordered_street_array[0].replace(",", "").strip()
        streets.append({"street": streetname, "housenumber": housenumber})
    json_streets = json.dumps(streets, ensure_ascii=False)
    return json_streets
