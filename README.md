# LAB - Class 33

## Project: drf-auth

## Author: Cole Gibbs

## Links and Resources

My class notes along with the class repo.

## PORT - 0.0.0.0

## How to initialize/run your application (where applicable)

1. `install -r requirements.txt`
2. `docker compose up`
3. `docker compose run web bash`
4. `python manage.py migrate`

## Tests

How do you run tests?

1. `docker compose up`
2. `docker compose run web bash`
3. `python manage.py test`

Any tests of note?

I don't have any tests to note.

Describe any tests that you did not complete, skipped, etc

All test passing.

## Routes

For token path, username and password go under Form-encode. For the refresh path the token goes in the Form-encode.

1. `http://0.0.0.0:8000/api/token/refresh`
2. `http://0.0.0.0:8000/api/token/`
3. `http://0.0.0.0:8000/api/v1/books/`
4. `http://0.0.0.0:8000/api/v1/books/1/`