import json
import unittest
from typing import Tuple

import pytest

from app.main import call_all_processors as call_all_processors_main
from app.main import (
    get_public_methods_from_processor as get_public_methods_from_processor_main,
)
from app.main import init_processor as init_processor_main
from app.main import init_repository as init_repository_main
from app.main import init_validator as init_validator_main
from app.services.processor import Processor
from app.services.repository import Repository
from app.services.validator import Validator

case = unittest.TestCase()
case.maxDiff = None


@pytest.fixture
def init_processor() -> Processor:
    """
    Processor initialization test, returns processor.
    """
    processor = Processor()
    return processor


@pytest.fixture
def init_repository() -> Repository:
    """
    Repository initialization test, returns repository.
    """
    repository = Repository()
    return repository


@pytest.fixture
def init_validator() -> Validator:
    """
    Validator initialization test, returns validator.
    """
    validator = Validator()
    return validator


@pytest.fixture
def simple_street_data_sample() -> list:
    """
    Function to create testing simple data list ,
    returns simple data list.
    """

    return ["Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B"]


@pytest.fixture
def middle_street_data_sample() -> list:
    """
    Function to create testing middle data list ,
    returns middle (more data comparing to simple) data list.
    """

    return [
        "Winterallee 3",
        "Musterstrasse 45",
        "Blaufeldweg 123B",
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
    ]


@pytest.fixture
def complex_street_data_sample() -> list:
    """
    Function to create testing complex data list,
    returns complex (more data comparing to complex) data list.
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


@pytest.fixture
def expected_simple_data_sample() -> str:
    """
    Function to create testing expected simple data json object,
    returns simple (more data comparing to simple) data json object.
    """

    return json.dumps(
        [
            {"street": "Winterallee", "housenumber": "3"},
            {"street": "Musterstrasse", "housenumber": "45"},
            {"street": "Blaufeldweg", "housenumber": "123B"},
        ],
        ensure_ascii=False,
    )


@pytest.fixture
def expected_middle_data_sample() -> list:
    """
    Function to create testing expected middle data json object,
    returns middle (more data comparing to simple) data json object.
    """

    return json.dumps(
        [
            {"street": "Winterallee", "housenumber": "3"},
            {"street": "Musterstrasse", "housenumber": "45"},
            {"street": "Blaufeldweg", "housenumber": "123B"},
            {"street": "Am Bächle", "housenumber": "23"},
            {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
        ],
        ensure_ascii=False,
    )


@pytest.fixture
def expected_complex_data_sample() -> str:
    """
    Function  to create testing expected complex data json object,
    returns  complex(more data comparing to middle) data json object.
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


@pytest.fixture
def validation_data(expected_complex_data_sample) -> Tuple[float, str]:
    """
    Function  to test validate_data(),
    takes expected complex data json object
    returns a tuple with  accuracy and  expected complex data json object.
    """
    perfect_accuracy = 100.0
    return perfect_accuracy, expected_complex_data_sample


@pytest.fixture
def get_public_methods_from_processor() -> list:
    """
    Function to create testing list with all public methods from processor,
    returns a list with all public methods from processor.
    """
    return [
        "complex_deepparse_processor",
        "complex_processor",
        "middle_processor",
        "simple_processor",
    ]


@pytest.fixture
def call_all_processors():
    """
    Function to create testing list with the results of
    processing complex data with all different processors,
    returns a list of dicts with method and all the processed data.
    """
    return [
        {
            "method": "complex_deepparse_processor",
            "processed_data": '[{"street": "Winterallee", "housenumber": "3"}, {"street": "Musterstrasse", "housenumber": "45"}, {"street": "Blaufeldweg", "housenumber": "123b"}, {"street": "Am bächle", "housenumber": "23"}, {"street": "Auf der vogelwiese", "housenumber": "23 b"}, {"street": "Rue de la", "housenumber": "4"}, {"street": "Broadway av", "housenumber": "200"}, {"street": "Calle aduana", "housenumber": "29"}, {"street": "Calle", "housenumber": "39"}]',
        },
        {
            "method": "complex_processor",
            "processed_data": '[{"street": "Winterallee", "housenumber": "3"}, {"street": "Musterstrasse", "housenumber": "45"}, {"street": "Blaufeldweg", "housenumber": "123B"}, {"street": "Am Bächle", "housenumber": "23"}, {"street": "Auf der Vogelwiese", "housenumber": "23b"}, {"street": "rue de la revolution", "housenumber": "4"}, {"street": "Broadway Av", "housenumber": "200"}, {"street": "Calle Aduana", "housenumber": "29"}, {"street": "39 No 1540", "housenumber": "Calle "}]',
        },
        {
            "method": "middle_processor",
            "processed_data": '[{"street": "Winterallee", "housenumber": "3"}, {"street": "Musterstrasse", "housenumber": "45"}, {"street": "Blaufeldweg", "housenumber": "123B"}, {"street": "Am Bächle", "housenumber": "23"}, {"street": "Auf der Vogelwiese", "housenumber": "23 b"}, {"street": "", "housenumber": ""}, {"street": "", "housenumber": ""}, {"street": "Calle Aduana", "housenumber": ", 29"}, {"street": "Calle", "housenumber": "39 No 1540"}]',
        },
        {
            "method": "simple_processor",
            "processed_data": '[{"street": "Winterallee", "housenumber": "3"}, {"street": "Musterstrasse", "housenumber": "45"}, {"street": "Blaufeldweg", "housenumber": "123B"}, {"street": "", "housenumber": ""}]',
        },
    ]


def test_simple_processor(
    init_processor, simple_street_data_sample, expected_simple_data_sample
):
    """
    Simple processor testing function,
    takes a processor instance, unprocessed simple data and expected simple data,
    returns badly processed streets.
    """
    actual = json.loads(
        Processor.simple_processor(init_processor, simple_street_data_sample)
    )
    expected = json.loads(expected_simple_data_sample)
    case.assertEqual(actual, expected)


def test_middle_processor(
    init_processor, middle_street_data_sample, expected_middle_data_sample
):
    """
    Middle processor testing function,
    takes a processor instance, unprocessed middle data and expected middle data,
    returns badly processed streets.
    """
    actual = json.loads(
        Processor.middle_processor(init_processor, middle_street_data_sample)
    )
    expected = json.loads(expected_middle_data_sample)
    case.assertEqual(actual, expected)


def test_complex_processor(
    init_processor, complex_street_data_sample, expected_complex_data_sample
):
    """
    Complex processor testing function,
    takes a processor instance, unprocessed complex data and expected complex data,
    returns badly processed streets.
    """
    actual = json.loads(
        Processor.complex_processor(init_processor, complex_street_data_sample)
    )

    expected = json.loads(expected_complex_data_sample)
    case.assertCountEqual(actual, expected)


def test_complex_deeparse_processor(
    init_processor, complex_street_data_sample, expected_complex_data_sample
):
    """
    Complex processor testing function,
    takes a processor instance, unprocessed complex data and expected complex data,
    returns badly processed streets.
    """
    actual = json.loads(
        Processor.complex_deepparse_processor(
            init_processor, complex_street_data_sample
        )
    )
    expected = json.loads(expected_complex_data_sample)
    case.assertCountEqual(actual, expected)


def test_get_complex_data(init_repository, complex_street_data_sample):
    """
    Repository getter testing function,
    returns complex (all streets) data json object.
    """
    actual = Repository.get_complex_data(init_repository)
    expected = complex_street_data_sample
    case.assertCountEqual(actual, expected)


def test_get_expected_complex_data(
    init_repository, expected_complex_data_sample
):
    """
    Repository getter testing function,
    takes repository and expected complex data json object
    returns difference between actual (from repository) and expected data.
    """
    actual = json.loads(Repository.get_expected_complex_data(init_repository))
    expected = json.loads(expected_complex_data_sample)
    case.assertCountEqual(actual, expected)


def test_validate_data(
    init_validator,
    expected_complex_data_sample,
    validation_data,
):
    """
    Main validate data testing function,
    takes validator, expected complex data json object and expected complex validated data json object
    and returns difference between actual (from main function) and expected data.
    """
    actual = expected_complex_data_sample
    expected = expected_complex_data_sample
    actual_accuracy, actual_matching_list = Validator.validate_data(
        init_validator, actual, expected
    )
    expected_accuracy, expected_matching_list = validation_data
    expected_matching_list = json.loads(expected_matching_list)
    case.assertCountEqual(actual_matching_list, expected_matching_list)
    case.assertEqual(actual_accuracy, expected_accuracy)


def test_init_processor():
    """
    Testing function for processor initialization function,
    returns true if processor is created
    """
    case.assertIsNotNone(init_processor_main())


def test_init_repository():
    """
    Testing function for repository initialization function,
    returns true if repository is created
    """
    case.assertIsNotNone(init_repository_main())


def test_init_validator():
    """
    Testing function for validator initialization function,
    returns true if validator is created
    """
    case.assertIsNotNone(init_validator_main())


def test_get_public_methods_from_processor(
    get_public_methods_from_processor, init_processor
):
    """
    Testing function for getter of public methods from processor function,
    returns difference between actual (main function) public method list
    and expected public  method list.
    """
    case.assertCountEqual(
        get_public_methods_from_processor,
        get_public_methods_from_processor_main(init_processor),
    )


def test_call_all_processors(
    call_all_processors,
    get_public_methods_from_processor,
    init_processor,
    init_repository,
):
    """
    Testing function for call all processors function,
    returns difference between actual (main function)  public method list and
    expected methods and streets list.
    """
    case.assertCountEqual(
        call_all_processors,
        call_all_processors_main(
            get_public_methods_from_processor, init_processor, init_repository
        ),
    )
