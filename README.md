# Feed line application with user's posts, achievements & a few ads


## Common

There are 2 release branches and 1 main branch. So select project version (**release_1.0** or **release_2.0**).


## Setup PostgreSQL database

```zsh
createdb -h localhost -p 5432 -U postgres event_wall
```


## Environmental values

Input following values to .env file
- DEBUG=1
- SECRET_KEY=your_Django_secret_key_here
- ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]
- DB_NAME=event_wall
- DB_USER=postgres
- DB_PASSWORD=1234
- DB_HOST=127.0.0.1

After that setup Poetry to have virtual environvental for application:

```zsh
poetry lock
poetry install
```


## Command order to run project:

```zsh
# Get project
## Copy project from GitHub
git clone git@github.com:RoTorEx/Event_feed_list.git


# Select project version
## First (beta)
git checkout release_1.0

## Or second (final)
git checkout release_2.0


# Main flow
## Make migrations
make migrate

## Clean database and again fill it.
make seed

## Run application
make run


# Other
## Only clean database
make flush

## Only fill database
make fill

## Run linters, formatters and code analysers
make lint
```


## Endpoints

_All enpoints below stars with **http://127.0.0.1:8000**_.

- [Swagger](http://127.0.0.1:8000/swagger/) - API Documentation
- [User/1](http://127.0.0.1:8000/api/v1/user/1/) - Feed for specific user by ID
- [Post/1](http://127.0.0.1:8000/api/v1/post/1) - Specific selected post by ID
- [Post/1/post_title_here](http://127.0.0.1:8000/api/v1/post/1/post_title_here/) - Specific selected post by title
- [Achievements/1](http://127.0.0.1:8000/api/v1/achievement/1) - Specific selected achievement by ID
