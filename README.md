# FRIDAY_code_challenge
Code challenge for FRIDAY enterprise

# Problems
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
