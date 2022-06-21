import json


class Repository:
    """
    Repository with all the data to process and its expected results.
    """

    def get_complex_data(self) -> list:
        """
        Function that return complex data list.
        """
        return [
            "Winterallee 3",
            "Musterstrasse 45",
            "Blaufeldweg 123B",
            "Am Bächle 23",
            "Auf der Vogelwiese 23 b",
            "4, rue de la revolution",
            "200 Broadway Av",
            "Calle Aduana, 29",
            "Calle 39 No 1540",
        ]

    def get_expected_complex_data(self) -> str:
        """
        Function that return complex data list.
        """
        return json.dumps(
            [
                {"street": "Winterallee", "housenumber": "3"},
                {"street": "Musterstrasse", "housenumber": "45"},
                {"street": "Blaufeldweg", "housenumber": "123B"},
                {"street": "Am Bächle", "housenumber": "23"},
                {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
                {"street": "rue de la revolution", "housenumber": "4"},
                {"street": "Broadway Av", "housenumber": "200"},
                {"street": "Calle Aduana", "housenumber": "29"},
                {"street": "Calle 39", "housenumber": "No 1540"},
            ],
            ensure_ascii=False,
        )
