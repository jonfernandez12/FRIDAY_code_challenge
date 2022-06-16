import re
import json
from ast import Str

def middle_processor(concatenated_street: Str, test: json) -> json:

    """
    Function that reads concatenated street and
    returns street name and number json object
    """
    street = re.findall('([a-zA-Z \u0080-\uFFFF]*)\d*.*',concatenated_street)
    housenumber = concatenated_street.split(street[0],1)

    x = {"street": street[0].strip(), "housenumber": housenumber[1].strip()}
    
    complete_street = json.dumps(x, ensure_ascii=False)

    print(complete_street)
    print(test)
    print(complete_street == test)
