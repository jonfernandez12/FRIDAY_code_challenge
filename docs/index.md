# FRIDAY_code_challenge
Code challenge for FRIDAY enterprise

# Get started

# Modus operandi

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

4. We found a good regex that works 8/9 of the times (all streets but Calle 39 No 1540) , we are going to try another kind of process to parse streets.
```
"^(\b\D+\b)?\s*(\b.*?\d.*?\b)\s*(\b\D+\b)?$"
```

5. We achieve to parse the last street using:
```
(.*?)\s*(\d+(?:[/-]\d+)?)?$
```

5. We found an [state-of-the-art library for parsing multinational street addresses using deep learning](https://github.com/GRAAL-Research/deepparse), let's see how it works.

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
We try a pretrained machine learning clasificator to see if we get better results than the regex method, we need to understand how to extract data from the output returned by the model and which models where available using the library and which one was better for this purpose
```{bibliography}
    author = {Marouane Yassine and David Beauchemin},
    title  = {{Deepparse: A State-Of-The-Art Deep Learning Multinational Addresses Parser}},
    year   = {2020},
    note   = [url](https://deepparse.org)
```
---
deepparse,

---
## Testing
We discovered [helpful documentation](https://realpython.com/pytest-python-testing/) about python testing as I am not use to make tests although I knew about TDD, 