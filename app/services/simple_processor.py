import json


def simple_processor(concatenated_streets: list) -> json:

    """
    Function that reads simple concatenated street list and
    returns street name and number json object
    """
    streets = []
    for concatenated_street in concatenated_streets:
        [streetname, housenumber] = concatenated_street.split()
        streets.append({"street": streetname, "housenumber": housenumber})

    json_streets = json.dumps(streets, ensure_ascii=False)
    return json_streets
