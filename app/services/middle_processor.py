import re
import json
from ast import Str


def middle_processor(concatenated_streets: list) -> json:

    """
    Function that reads concatenated street list and
    returns street name and number json object
    """
    streets = []
    for concatenated_street in concatenated_streets:
        street = re.findall("([a-zA-Z \u0080-\uFFFF]*)\d*.*", concatenated_street)
        housenumber = concatenated_street.split(street[0], 1)

        streets.append(
            {
                "street": street[0].strip(),
                "housenumber": housenumber[1].strip()
            }
        )

    json_street = json.dumps(streets, ensure_ascii=False)
    return json_street
