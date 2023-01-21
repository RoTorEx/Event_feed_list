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

P.S. Before _`make seed`_ you can setup number of seeding entities change the range on 'USER', 'POST', 'ACHIEVEMENT', 'ADVERTISING' is **[here](./app/management/commands/seed.py)**.


## Endpoints

_All enpoints below stars with **http://127.0.0.1:8000**_.
Except for /users/, all handpoints only support a **GET** request. At /users/ **all** actions are allowed

- [Swagger](http://127.0.0.1:8000/swagger/) - API Documentation
- [Endposint list](http://127.0.0.1:8000/api/v1/)
- [User](http://127.0.0.1:8000/api/v1/users/) - Users
- [User/1](http://127.0.0.1:8000/api/v1/users/1) - Specific selected user by ID
- [Posts](http://127.0.0.1:8000/api/v1/posts/) - Posts
- [Posts/1](http://127.0.0.1:8000/api/v1/posts/) - Specific selected post by ID
- [Achievements](http://127.0.0.1:8000/api/v1/achievements/) - Achievements
- [Achievements/1](http://127.0.0.1:8000/api/v1/achievements/) - Specific selected achievement by ID
- [Advertising](http://127.0.0.1:8000/api/v1/ads/) - Advertising
- [Advertising](http://127.0.0.1:8000/api/v1/ads/1) - Specific selected advertising by ID
- [Feed](http://127.0.0.1:8000/api/v1/feed/) - Nothing interesting here, just a few advertisements. Able use query params.
- [Feed/1](http://127.0.0.1:8000/api/v1/feed/1) - Feed list for each specific selected user by ID].  Here able to use query params to each customer:
  - [Feed/1?event_type=post](http://127.0.0.1:8000/api/v1/feed/1/?event_type=post) - Show all post specific selected user by ID
  - [Feed/1?event_type=achievement](http://127.0.0.1:8000/api/v1/feed/1/?event_type=achievement) - Show all achievements specific selected user by ID
