# LAB - Class 32

## Project: drf-api-permissions

## Author: Cole Gibbs

## Links and Resources

My class notes along with the class repo.

## PORT - 0.0.0.0

## How to initialize/run your application (where applicable)

1. `install -r requirements.txt`
2. `docker compose up`
3. `docker compose run web bash`

## Tests

How do you run tests?

1. `python manage.py test`

Any tests of note?

I don't have any tests to note.

Describe any tests that you did not complete, skipped, etc

I have two tests failing at the moment. One is to update the data and the other is to delete the data. I suspect they are not working because of the permission limitations required in this lab. I am unsure of how to adjust the test to account for permissions.
