# Modus operandi

[2022-06-16]
1. Read statement

2. Free thinking: 
    - First challenge looks easy, thinking about split() / strip(). 
    - Second challenge also easy, read until a numeric is found.
    - Third challenge looks like it needs another field such as postal code or an IA app to identify the country so as to know how to split streets or maybe an IA that learns how to split streets. 
    - Do I need a country, street and number database to cover all cases? 

3. Looks like regex is needed for the second challenge, did not think about german dictionary, is not going to be easy.
    - [Nice link!](https://regex101.com/r/fi5Ca2/1)
    -  [Nice link 2!](https://stackoverflow.com/questions/55774903/regular-expression-to-split-a-street-address-that-may-have-optional-numbers-with)
    ![Regex Example](regex_example.png)
    - Need to try to understand how does regex exactly works and adapt to my needs.

[2022-06-17]
4. We found a good regex that works 7/9 of the times (all streets but "4, rue de la revolution" and "Calle 39 No 1540") , we are going to try another kind of process to parse streets.
```
"^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$"
```

5. We found an [state-of-the-art library for parsing multinational street addresses using deep learning](https://github.com/GRAAL-Research/deepparse), let's see how it works.

[2022-06-19]
6. We read again the challenge statement and as we where blocked with 8/9 parsed streets, we decide to start using TDD and use as many python best practices as we can, incorporating the following concepts:
- Start developing following TDD, this is, start using automated unit tests to drive the development of our code.
- Add code formatting frameworks such as Black, Flake8 and Isort and automatizing code format checks whenever a commit was done.
- Add Makefile so it simplifies code running, testing and formatting no matter what IDE is being used.
- Add docs folder and organizing better documentation. Also adding testing and coverage reports into the documentation.


[2022-06-21]
7.  Understand how Actions in github work, trying to automate the execution of all docs an leave  them in public/ folder.
8. Thinking about how to organize project. (from functions to classes and main execution)
9. Add  json validation

# Faced problems
## Multiple SSH keys on same machine
1. To clone and interact with another github account, just create a new ssh-key:

```
ssh-keygen -t rsa
```

2. Save it on **/home/jon/.ssh/** with a different name if one already exists.
 
```
 ssh-add ~/.ssh/<new_private_key_file>  
 ```

3. Copy public key and paste on Github>Settings>SSH and GPG keys

4. Add configuration on **/home/jon/.ssh/config**
```
  Host <alias_name>
    Hostname github.com
    User git
    IdentityFile ~/.ssh/<new_private_key_file> 
    IdentitiesOnly yes
 ```
 5. Finally clone repository with 
  ```
 git clone <alias_name>:<github_name>/<proyect_name>.git
 ```
## REGEX
We need to learn what was regex from the very beginning, we find some useful websites as that given a regex explain what was deifning each character.
## Deepparse
We try a pre-trained machine learning classification method to see if we get better results than with the regex method, we need to understand how to extract data from the output returned by the model and which models where available using the library and which one was better for this purpose. As if we were not worried about cpu limitations we used 'best' model.

 ```{bibliography}
    author = {Marouane Yassine and David Beauchemin},
    title  = {{Deepparse: A State-Of-The-Art Deep Learning Multinational Addresses Parser}},
    year   = {2020},
    note   = [url](https://deepparse.org)
```
## Testing
We discovered [helpful documentation](https://realpython.com/pytest-python-testing/) about python testing. We  about fixtures as we are not used to make tests. Although we knew about TDD methodology.

Also, we modify the output of tests from a boolean type to a comparison between actual processed streets and expected streets, as a boolean gives no information about which streets are well parsed and which not. We did not find out a good library for asserting json lists so we convert them into python lists first and so we could make use of unittest TestCase library.

## Pipenv
Somehow, **pipenv run** commands was not working, giving us the following error:
```
Traceback (most recent call last):
File "/usr/bin/pipenv", line 11, in <module>
  load_entry_point('pipenv==11.9.0', 'console_scripts', 'pipenv')()
File "/usr/lib/python3/dist-packages/pipenv/vendor/click/core.py", line 722, in __call__
  return self.main(*args, **kwargs)
File "/usr/lib/python3/dist-packages/pipenv/vendor/click/core.py", line 697, in main
  rv = self.invoke(ctx)
File "/usr/lib/python3/dist-packages/pipenv/vendor/click/core.py", line 1066, in invoke
  return _process_result(sub_ctx.command.invoke(sub_ctx))
File "/usr/lib/python3/dist-packages/pipenv/vendor/click/core.py", line 895, in invoke
  return ctx.invoke(self.callback, **ctx.params)
File "/usr/lib/python3/dist-packages/pipenv/vendor/click/core.py", line 535, in invoke
  return callback(*args, **kwargs)
File "/usr/lib/python3/dist-packages/pipenv/cli.py", line 602, in run
  core.do_run(command=command, args=args, three=three, python=python)
File "/usr/lib/python3/dist-packages/pipenv/core.py", line 2200, in do_run
  command = ' '.join(project.scripts[command])
File "/usr/lib/python3/dist-packages/pipenv/project.py", line 374, in scripts
  scripts[k] = shlex.split(v, posix=True)
File "/usr/lib/python3.8/shlex.py", line 311, in split
  return list(lex)
File "/usr/lib/python3.8/shlex.py", line 300, in __next__
  token = self.get_token()
File "/usr/lib/python3.8/shlex.py", line 109, in get_token
  raw = self.read_token()
File "/usr/lib/python3.8/shlex.py", line 140, in read_token
  nextchar = self.instream.read(1)
AttributeError: 'list' object has no attribute 'read'
 ```

 We fix it reinstalling pipenv:

```
sudo apt-get remove pipenv
pip3 install pipenv
 ```

 ## Flake8
 Makes the following warning:
 ```
 ./app/services/middle_processor.py:14:39: W605 invalid escape sequence '\d'
 ```
 It seems that Python 3 interprets string literals as Unicode strings, and therefore our \d is treated as an escaped Unicode character. As we are following [Flake8 rules regarding W605](https://www.flake8rules.com/rules/W605.html)  and [Flake8 rules regarding W503](https://www.flake8rules.com/rules/W503.html) to avoid the warning we add --ignore flag when checking flake8 format:

 ```
check-flake8 = "python -m flake8 --exclude=.venv/ --ignore=W605"
 ```
 Even so, a warning is raised when we run tests with pytest. 