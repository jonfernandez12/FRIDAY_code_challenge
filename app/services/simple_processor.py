import json
from ast import Str


def simple_processor(concatenated_street: Str, test: json) -> json:

    """
    Function that reads simple concatenated street and
    returns street name and number json object
    """

    [street, housenumber] = concatenated_street.split()
    x = {"street": street, "housenumber": housenumber}
    complete_street = json.dumps(x)

    print(complete_street == test)
