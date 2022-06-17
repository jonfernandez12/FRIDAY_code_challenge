import re
import json
from ast import Str

from yaml import parse
from deepparse.parser import AddressParser

def complex_deepparse_processor(concatenated_streets: list) -> json:

    """
    Function that reads complex concatenated street and
    returns street name and number json object
    """
    address_parser = AddressParser(model_type="best", device=0)
    streets=[]
    for concatenated_street in concatenated_streets:
        parsed_address = address_parser(concatenated_street)
        streets.append(
            {
                "street": parsed_address.StreetName, 
                "housenumber": parsed_address.StreetNumber
            }
        )

    json_streets = json.dumps(streets, ensure_ascii=False)
    return json_streets
