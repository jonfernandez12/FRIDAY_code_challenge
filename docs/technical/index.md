# Techinal documentation

The following section will cover technical aspects of the development.

## Code Structure
The selected code structure has been designed based on the purpose I was asked, this is, data processing. First of all I start thinking about the processor, without taking care of how I was initializing data. Second, came testing, so as to validate data and develop processors at the same time. Then, the need for a repository came up, because data need to be initialized in a proper and secure way and looking into future to possible connections to database.  Last, when I was developing the main thread, the need for a validation and proper results arose. Also together with validation a proper way of logging was needed and I created a logger.

### Repository
The repository class is meant to be the one that accesses the data, most commonly a database. In this case, only plays the role of getter as data is hardcoded. From this class I can obtain raw data as well as expected data.

### Processor
Processor, as the world itself describes it, has all the methods to process the data:
- simple processor: First approach, it was meant to process simplest data, this is, data from task 1. 
- middle processor: Second approach, it was meant to process middle complex data, this is, data from task 2. 
- complex processor: Third approach, it was meant to process more complex data, this is, data from task 3. 
- complex deeparse processor: Fourth approach, it was meant to process complex data using machine learning classificator. 

### Validator
Finally, the validator, only has one method and is used to validate data between the streets I have processed and the expected ones, It gives us information about how many streets have been successfully processed and which are them. 

### Testing
For testing pytest and unittest have been used, at first, I try to compare json objects but then I figures out it was easier to compare python lists using assertCountEqual() function. Also pytest fixtures have been used to provide fixed data and instances for the tests. 

## Documentation
Plenty documentation is offered, coverage documentation with coverage library, format related documentation using Flake8 and project documentation using mkdocs. 

## Makefile
Finally a makefile have been provided so that program execution, testing and documenting is easier and more flexible when switching between IDEs. Also some tasks have been automatized, for example, when "make docs" command is executed, all tests, coverage and markdown text is processed and grouped in html format in public/ folder. Is worth mentioning that Makefile interacts also with Pipfile, as they have been described also less abstract scripts in this file. For example the command flow for command "make format" would be the following:

| Makefile              |          Pipfile                        | Python
| ------------------------| ---------------------------------- |-----------------------------------------------------------------------
| make format      | pipenv run black &&      | python -m black . &&
|                                | pipenv run isort              | python -m isort --sp pyproject.toml --skip .venv .

