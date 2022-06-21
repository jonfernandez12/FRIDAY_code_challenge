import json


class Validator:

    """
    Class for validate data.
    """

    def validate_data(self, actual: str, expected: str) -> tuple[float, list]:
        """
        Function that given an actual json list and expected json
        list, transforms the data into lists and returns matching
        percentage and matching items between lists.
        """
        actual_data = json.loads(actual)
        expected_data = json.loads(expected)
        list_difference = []
        for item in expected_data:
            if item in actual_data:
                list_difference.append(item)
        matching_percentage = len(list_difference) / len(expected_data) * 100
        return matching_percentage, list_difference
