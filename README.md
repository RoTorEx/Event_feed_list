# Django newsline app


## Environmental values

Input following values to .env file
- DEBUG=1
- SECRET_KEY=your_Django_secret_key_here
- ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
- DB_NAME=newsline
- DB_USER=postgres
- DB_PASSWORD=1234
- DB_HOST=127.0.0.1

After that setup Poetry to have virtual environvental for application:

```zsh
poetry lock
poetry install
```


## Command order to start project:

```zsh
# Main flow
## Make migrations
make migrate

## Clean database and again fill it
make seed

## Run application
make run

# Other
## Only clean database
make flush

## Only fill database
make fill
```
