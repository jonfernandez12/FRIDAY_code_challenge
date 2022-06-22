import json

from services.logger import logger
from services.processor import Processor
from services.repository import Repository
from services.validator import Validator

__version__ = "0.0.1"
"""
Application for splitting concatenated street names and numbers into
formatted json objects using different processors.
"""


def init_validator() -> Validator:
    """
    Validator initialization function, returns validator.
    """
    logger.info("Creating data validator, please wait...")
    try:
        validator = Validator()
        logger.info("\u2728  Success creating data validator!  \u2728")
    except Exception as e:
        logger.error(
            "\u274C Error creating data validator, " + str(e) + "\u274C"
        )
    return validator


def init_processor() -> Processor:
    """
    Processor initialization function, returns processor.
    """
    logger.info("Creating data processor, please wait...")
    try:
        processor = Processor()
        logger.info("\u2728  Success creating data processor!  \u2728")
    except Exception as e:
        logger.error(
            "\u274C Error creating data processor, " + str(e) + "\u274C"
        )
    return processor


def init_repository() -> Repository:
    """
    Repository initialization function, returns repository.
    """
    logger.info("Accessing data with the repository, please wait...")
    try:
        repository = Repository()
        logger.info("\u2728  Success getting data with the repository!  \u2728")
    except Exception as e:
        logger.error(
            "\u274C Error accessing data with the repository, "
            + str(e)
            + "\u274C"
        )
    return repository


def get_public_methods_from_processor(processor: Processor) -> list:
    """
    Function that takes processor instance and
    returns all processor methods.
    """
    public_method_names = [
        method
        for method in dir(processor)
        if callable(getattr(processor, method))
        if not method.startswith("_")
    ]
    return public_method_names


def call_all_processors(
    public_method_names: list, processor: Processor, repository: Repository
) -> list:
    """
    Function that takes processor instance, repository instance and
    all public methods name from processor instance and
    returns a list of dicts formed by method and processed street data.
    """
    processed_data = []
    for method in public_method_names:
        processed_data.append(
            {
                "method": method,
                "processed_data": getattr(processor, method)(
                    repository.get_complex_data()
                ),
            }
        )
    return processed_data


def validate_data(processed_data: list) -> None:
    """
    Function that takes processed data, then validates processed data and logs
    which accuracy has had each method when processing data and which streets
    has properly processed.
    """
    for processed in processed_data:

        method = str(processed["method"]).capitalize().replace("_", " ")
        logger.info(
            "-----------------------------------------\U0001f3af "
            + method
            + " results:\U0001f3af-----------------------------------------"
        )
        accuracy_percentage, list_difference = validator.validate_data(
            processed["processed_data"],
            repository.get_expected_complex_data(),
        )
        logger.info("\033[1m Well processed streets are:\033[0m")
        for item in list_difference:
            logger.info("\t" + str(item))
        logger.info(
            "\033[1m Percentage of accuracy of is: "
            + str(round(accuracy_percentage))
            + "%  \u2705 \033[0m"
        )


if __name__ == "__main__":
    logger.info("Service started with version {}".format(__version__))

    processor = init_processor()
    repository = init_repository()
    validator = init_validator()

    logger.info(
        "----------------------------------------Expected results-----------------------------------------"
    )
    expected_data = json.loads(repository.get_expected_complex_data())
    for item in expected_data:
        logger.info("\t" + str(item))

    try:

        public_method_names = get_public_methods_from_processor(processor)
        processed_data = call_all_processors(
            public_method_names, processor, repository
        )

        validate_data(processed_data)

    except Exception as e:
        logger.error("\u274C Error validating data, " + str(e) + "\u274C")
