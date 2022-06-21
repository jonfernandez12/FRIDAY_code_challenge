
# Faced problems

The following section will cover the problems I have face during challenge implementation.

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

## Regex
I need to learn what is regex from the very beginning, we find some useful websites as that given a regex explain what was defining each character. Finally I decided to use "^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$" as is the one with better splitting results.

## Deepparse
We try a pre-trained machine learning classification method to see if we get better results than with the regex method, we need to understand how to extract data from the output returned by the model and which models where available using the library and which one was better for this purpose. As if we were not worried about cpu limitations we used 'best' model.

 ```{bibliography}
    author = {Marouane Yassine and David Beauchemin},
    title  = {{Deepparse: A State-Of-The-Art Deep Learning Multinational Addresses Parser}},
    year   = {2020},
    note   = [url](https://deepparse.org)
```
## Testing
I discovered [helpful documentation](https://realpython.com/pytest-python-testing/) about python testing and fixtures as I am not used to make tests. Although I knew about TDD methodology.

Also, I modify the output of tests from a boolean type to a comparison between actual processed streets and expected streets, as a boolean gives no information about which streets are well parsed and which not. I did not find out a good library for asserting json lists so we convert them into python lists first, so I could make use of unittest TestCase library.

## Pipenv
Somehow, **pipenv run** commands was not working, giving the following error:
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

 I fix it reinstalling pipenv:

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