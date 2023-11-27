# Rosa

Voting application created as term project for WSB
Named after Rosa Luxemburg - great advocate for democracy and voting

## Architecture

### config

Config taken from json file

Config elements:
* Token 
* * duration

* Database  
* * credentials
* * host

### Authentication
 Login/password gives you JWT, that is used for all other services.
 * config - token duration


## TODO

##Database
### Users table
Permisions
* 0 - regular user
* 1 - moderator (as regular user + managing votings)
* 2 - admin (as moderator + managing users)

### Login endpoint
Post endpoint, that accepts JSON payload with user/pass
Hashes pass
gets hash from db
if there is one- compares

## Nice to have
* avoid plaintext passwords - get them from env