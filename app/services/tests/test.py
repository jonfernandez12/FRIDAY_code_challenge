import json
import unittest

import pytest

from app.services.processor import Processor

case = unittest.TestCase()
case.maxDiff = None


@pytest.fixture
def init_processor() -> Processor:
    processor = Processor()
    return processor


@pytest.fixture
def simple_street_data_sample() -> list:

    return ["Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B"]


@pytest.fixture
def middle_street_data_sample() -> list:

    return [
        "Winterallee 3",
        "Musterstrasse 45",
        "Blaufeldweg 123B",
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
    ]


@pytest.fixture
def complex_street_data_sample() -> list:

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


def test_simple_processor(init_processor, simple_street_data_sample):
    actual = json.loads(
        Processor.simple_processor(init_processor, simple_street_data_sample)
    )
    expected = json.loads(
        json.dumps(
            [
                {"street": "Winterallee", "housenumber": "3"},
                {"street": "Musterstrasse", "housenumber": "45"},
                {"street": "Blaufeldweg", "housenumber": "123B"},
            ],
            ensure_ascii=False,
        )
    )
    case.assertEqual(actual, expected)


def test_middle_processor(init_processor, middle_street_data_sample):
    actual = json.loads(
        Processor.middle_processor(init_processor, middle_street_data_sample)
    )
    expected = json.loads(
        json.dumps(
            [
                {"street": "Winterallee", "housenumber": "3"},
                {"street": "Musterstrasse", "housenumber": "45"},
                {"street": "Blaufeldweg", "housenumber": "123B"},
                {"street": "Am Bächle", "housenumber": "23"},
                {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
            ],
            ensure_ascii=False,
        )
    )
    case.assertEqual(actual, expected)


def test_complex_processor(init_processor, complex_street_data_sample):
    actual = json.loads(
        Processor.complex_processor(init_processor, complex_street_data_sample)
    )

    expected = json.loads(
        json.dumps(
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
    )
    case.assertCountEqual(actual, expected)


def test_complex_deeparse_processor(init_processor, complex_street_data_sample):
    actual = json.loads(
        Processor.complex_deepparse_processor(
            init_processor, complex_street_data_sample
        )
    )
    expected = json.loads(
        json.dumps(
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
    )
    case.assertCountEqual(actual, expected)
