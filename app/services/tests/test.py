import json
import pytest
from services.complex_deepparse_processor import complex_deepparse_processor
from services.complex_processor import complex_processor
from services.middle_processor import middle_processor
from services.simple_processor import simple_processor


@pytest.fixture
def simple_street_data_sample() -> list:

    return [
        "Winterallee 3",
        "Musterstrasse 45", 
        "Blaufeldweg 123B"
    ]


@pytest.fixture
def middle_street_data_sample() -> list:

    return [
            "Winterallee 3", 
            "Musterstrasse 45", 
            "Blaufeldweg 123B",
            "Am Bächle 23",
            "Auf der Vogelwiese 23 b"
    ]


@pytest.fixture
def complex_street_data_sample() -> list:

    return [
        "Winterallee 3", 
        "Musterstrasse 45",
         "Blaufeldweg 123B",
         "Am Bächle 23", 
         "Auf der Vogelwiese 23 b",
         "4, rue de la revolution","200 Broadway Av", 
         "Calle Aduana, 29", 
         "Calle 39 No 1540"
    ]



def test_simple_processor(simple_street_data_sample):

    assert simple_processor(simple_street_data_sample) == json.dumps(
        [
            {"street": "Winterallee", "housenumber": "3"},
            {"street": "Musterstrasse", "housenumber": "45"},
            {"street": "Blaufeldweg", "housenumber": "123B"}
        ],
        ensure_ascii=False,
    )

def test_middle_processor(middle_street_data_sample):

    assert middle_processor(middle_street_data_sample) == json.dumps(
        [
            {"street": "Winterallee", "housenumber": "3"},
            {"street": "Musterstrasse", "housenumber": "45"},
            {"street": "Blaufeldweg", "housenumber": "123B"},
            {"street": "Am Bächle", "housenumber": "23"},
            {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
        ],
        ensure_ascii=False,
    )

def test_complex_processor(complex_street_data_sample):

    assert complex_processor(complex_street_data_sample) == json.dumps(
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

def test_complex_deeparse_processor(complex_street_data_sample):

    assert complex_deepparse_processor(complex_street_data_sample) == json.dumps(
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


    

