import json
import re

from deepparse.parser import AddressParser
from services.logger import logger


class Processor:
    """
    Class with all the methods to process data.
    """

    def simple_processor(self, concatenated_streets: list) -> str:

        """
        Function that reads simple concatenated street list and
        returns street name and number json object
        """
        streets = []
        try:
            for concatenated_street in concatenated_streets:
                [streetname, housenumber] = concatenated_street.split()
                streets.append(
                    {"street": streetname, "housenumber": housenumber}
                )
        except Exception as e:
            logger.error(
                "Error in simple processor splitting: "
                + concatenated_street
                + " street, "
                + str(e)
            )
            streets.append({"street": "", "housenumber": ""})
        json_streets = json.dumps(streets, ensure_ascii=False)
        return json_streets

    def middle_processor(self, concatenated_streets: list) -> str:

        """
        Function that reads concatenated street list and
        returns street name and number json object
        """
        streets = []
        for concatenated_street in concatenated_streets:
            try:
                street = re.findall(
                    "([a-zA-Z \u0080-\uFFFF]*)\d*.*", concatenated_street
                )
                housenumber = concatenated_street.split(street[0], 1)
                streets.append(
                    {
                        "street": street[0].strip(),
                        "housenumber": housenumber[1].strip(),
                    }
                )
            except Exception as e:
                logger.error(
                    "Error in middle processor splitting: "
                    + concatenated_street
                    + " street, "
                    + str(e)
                )
                streets.append({"street": "", "housenumber": ""})
        json_street = json.dumps(streets, ensure_ascii=False)
        return json_street

    def complex_processor(self, concatenated_streets: list) -> str:

        """
        Function that reads complex concatenated street list and
        returns street name and number json object
        """
        regex = r"^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$"
        streets = []
        try:
            for concatenated_street in concatenated_streets:
                street = re.findall(regex, concatenated_street)
                housenumber = ""
                street_array = []
                for item in street[0]:
                    street_array.append(item)

                ordered_street_array = sorted(
                    street_array, key=len, reverse=True
                )

                for index in range(1, len(ordered_street_array)):
                    housenumber = housenumber + ordered_street_array[index]
                streetname = ordered_street_array[0].replace(",", "").strip()
                streets.append(
                    {"street": streetname, "housenumber": housenumber}
                )
        except Exception as e:
            logger.error(
                "Error in complex processor splitting: "
                + concatenated_street
                + " street, "
                + str(e)
            )
            streets.append({"street": "", "housenumber": ""})
        json_streets = json.dumps(streets, ensure_ascii=False)
        return json_streets

    def complex_deepparse_processor(self, concatenated_streets: list) -> str:

        """
        Function that reads complex concatenated street and
        returns street name and number json object using deepparse model
        """
        address_parser = AddressParser(model_type="best", device=0)
        streets = []
        try:
            for concatenated_street in concatenated_streets:
                parsed_address = address_parser(concatenated_street)
                streets.append(
                    {
                        "street": parsed_address.StreetName.capitalize().strip(),
                        "housenumber": parsed_address.StreetNumber.strip(),
                    }
                )
        except Exception as e:
            logger.error(
                "Error in complex deepparse processor splitting: "
                + concatenated_street
                + " street, "
                + str(e)
            )
            streets.append({"street": "", "housenumber": ""})
        json_streets = json.dumps(streets, ensure_ascii=False)
        return json_streets
