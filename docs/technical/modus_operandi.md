# Modus operandi

The following section will cover which has been the procedure while developing the challenge.

[2022-06-16]

1. Read statement

2. Free thinking: 
    - First challenge looks easy, thinking about split() / strip(). 
    - Second challenge also easy, read until a numeric is found.
    - Third challenge looks like it needs another field such as postal code or an IA app to identify the country so as to know how to split streets or maybe an IA that learns how to split streets. 
    - Do I need a country, street and number database to cover all cases? 

3. Looks like regex is needed for the second challenge, did not think about german dictionary.

    - [Nice link!](https://regex101.com/r/fi5Ca2/1)
    -  [Nice link 2!](https://stackoverflow.com/questions/55774903/regular-expression-to-split-a-street-address-that-may-have-optional-numbers-with)
    ![Regex Example](regex_example.png)
    - Need to try to understand how does regex exactly works and adapt to my needs.

[2022-06-17]

4. I found a good regex that works 7/9 of the times (all streets but "4, rue de la revolution" and "Calle 39 No 1540") , I am going to try another kind of process to parse streets.
```
"^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$"
```

5. I found an [state-of-the-art library for parsing multinational street addresses using deep learning](https://github.com/GRAAL-Research/deepparse), let's see how it works.

[2022-06-19]

6. I read again the challenge statement and as I was blocked with some streets, I decide to start using TDD and use as many python best practices as I know, incorporating the following concepts:
- Start developing following TDD, this is, start using automated unit tests to drive the development of our code.
- Add code formatting frameworks such as Black, Flake8 and Isort and automatizing code format checks whenever a commit was done.
- Add Makefile so it simplifies code running, testing and formatting no matter what IDE is being used.
- Add docs folder and organizing better documentation. Also adding testing and coverage reports into the documentation.


[2022-06-21]

7.  Understand how Actions in github work, trying to automate the execution of all docs an leave  them in public/ folder, finally not achieved, I create public in local and uploaded to Github so is accessible via https://jonfernandez12.github.io/FRIDAY_code_challenge/public/.
8. Thinking about how to organize project. First 3 files where developed with one function each of them, then I think it was a better idea to create a Processor class, Repository class and Validator class to organize concepts in the code structure.
