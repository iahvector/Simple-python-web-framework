**NOTE:** This code is a solution for a challenge from a company that didn't want it to be public, so I've changed the company name here and inside the code into acme and removed all the git history so it can't be found in previous commits. [ACME](https://en.wikipedia.org/wiki/Acme_Corporation), obviously, is not a real company name

# ACME interview test: Recipes API

### How to use:
* Build the containers using
```
docker-compose build
```
* To run the app, use
```
docker-compose up
```
* To run the test, use
```
docker-compose  run --rm python run_tests
```
### API Documentation:
The API is documented using the OpenAPI standard. To view the documentation, start the containers, then go to http://localhost:8000

### Framework documentation
* The framework has been moved into it's own separate repo under the name of [PyExpress](https://github.com/iahvector/PyExpress)

---

## About the app:
### Technologies:
- Application programming language: Python 3.6
- Database: MongoDB 3.2.3
- Application server: Green Unicorn 19.7.1
- Web server: Nginx 1.12

### Architecture:
* The application architecture is inspired by [Alistair Cockburn's Hexagonal architecture](http://alistair.cockburn.us/Hexagonal+architecture) Where the business logic is kept independent from details like the database and the delivery method and the details are plugged in via ports.
* The router is based on [This example from WebOb's documentation](https://webob.readthedocs.io/en/stable/do-it-yourself.html). The intended design is to have the router accept other routers for routes to be able to pass modular and reusable apps so large apps will be composed from smaller apps. The design is inspired by NodeJS' expressJS.

### TODO:
* Add more unit tests. The current tests are meant to show the testability of the code, but they are by no means cover all the cases.
* Add end to end tests to test the REST APIs
* Implement the missing update and delete APIs
* Implement rating for recipes
* Implement users and authentication using JWT
* Modify the router to use classes instead of functions to be able to group resource logic in one class
* Modify the router to use middleware
* Implement authorization using middleware

-----------------------------------------------------------------------------------------------------------------------

# ACME Senior Backend Developer Test

Hello and thanks for taking the time to try this out.

The goal of this test is to assert (to some degree) your coding and architectural skills. You're given a simple problem so you can focus on showcasing development techniques. We encourage you to overengineer the solution a little to show off what you can do - assume you're building a production-ready application that other developers will need to work on and add to over time.

You're **allowed and encouraged** to use third party libraries, as long as you put them together yourself **without relying on a framework or microframework** to do it for you. An effective developer knows what to build and what to reuse, but also how his/her tools work. Be prepared to answer some questions about those libraries, like why you chose them and what other alternatives you're familiar with.

As this is a code review process, please avoid adding generated code to the project. This makes our jobs as reviewers more difficult, as we can't review code you didn't write. This means avoiding libraries like _Propel ORM_, which generates thousands of lines of code in stub files.

_Note: While we love open source here at ACME, please do not create a public repo with your test in! This challenge is only shared with people interviewing, and for obvious reasons we'd like it to remain this way._

## Prerequsites

We use [Docker](https://www.docker.com/products/docker) to administer this test. This ensures that we get an identical result to you when we test your application out, and it also matches our internal development workflows. If you don't have it already, you'll need Docker installed on your machine. **The application MUST run in the Docker containers** - if it doesn't we cannot accept your submission. You **MAY** edit the containers or add additional ones if you like, but this **MUST** be clearly documented.

We have provided some containers to help build your application in either PHP, Go or Python, with a variety of persistence layers available to use.

### Technology

- Valid PHP 7.1, Go 1.8, or Python 3.6 code
- Persist data to either Postgres, Redis, or MongoDB (in the provided containers).
    - Postgres connection details:
        - host: `postgres`
        - port: `5432`
        - dbname: `acme`
        - username: `acme`
        - password: `acme`
    - Redis connection details:
        - host: `redis`
        - port: `6379`
    - MongoDB connection details:
        - host: `mongodb`
        - port: `27017`
- Use the provided `docker-compose.yml` file in the root of this repository. You are free to add more containers to this if you like.

## Instructions

1. Clone this repository.
- Create a new branch called `dev`.
- Run `docker-compose up -d` to start the development environment.
    - If you want to use Go, uncomment the Go container in the `docker-compose.yml` file. Add the commands you need in there to execute the application.
    - If you want to use Python, uncomment the Python container in the `docker-compose.yml` file first. Add the commands you need in there to execute the application.
- Visit `http://localhost` to see the contents of the web container and develop your application.
- Create a pull request from your `dev` branch to the master branch. This PR should contain setup instructions for your application and a breakdown of the technologies & packages you chose to use, why you chose to use them, and the design decisions you made.
- Reply to the thread you're having with our HR department telling them we can start reviewing your code.

## Requirements

We'd like you to build a simple Recipes API. The API **MUST** conform to REST practices and **MUST** provide the following functionality:

- List, create, read, update, and delete Recipes
- Search recipes
- Rate recipes

### Endpoints

Your application **MUST** conform to the following endpoint structure and return the HTTP status codes appropriate to each operation. Endpoints specified as protected below **SHOULD** require authentication to view. The method of authentication is up to you.

##### Recipes

| Name   | Method      | URL                    | Protected |
| ---    | ---         | ---                    | ---       |
| List   | `GET`       | `/recipes`             | ✘         |
| Create | `POST`      | `/recipes`             | ✓         |
| Get    | `GET`       | `/recipes/{id}`        | ✘         |
| Update | `PUT/PATCH` | `/recipes/{id}`        | ✓         |
| Delete | `DELETE`    | `/recipes/{id}`        | ✓         |
| Rate   | `POST`      | `/recipes/{id}/rating` | ✘         |

An endpoint for recipe search functionality **MUST** also be implemented. The HTTP method and endpoint for this **MUST** be clearly documented.

### Schema

- **Recipe**
    - Unique ID
    - Name
    - Prep time
    - Difficulty (1-3)
    - Vegetarian (boolean)

Additionally, recipes can be rated many times from 1-5 and a rating is never overwritten.

## Evaluation criteria

These are some aspects we pay particular attention to:

- You **MUST** use packages, but you **MUST NOT** use a web-app framework or microframework.
- Your application **MUST** run within the containers. Please provide short setup instructions.
- The API **MUST** return valid JSON and **MUST** follow the endpoints set out above.
- You **MUST** write testable code and demonstrate unit testing it (for clarity,  PHPUnit is not considered a framework as per the first point above. We encourage you to use PHPUnit or any other kind of **testing** framework).
- You **SHOULD** pay attention to best security practices.
- You **SHOULD** follow SOLID principles where appropriate.
- You do **NOT** have to build a UI for this API.

The following earn you bonus points:

- Your answers during code review
- An informative, detailed description in the PR
- Setup with a one liner or a script
- Content negotiation
- Pagination
- Using any kind of Database Access Abstraction
- Other types of testing - e.g. integration tests
- Following the industry standard style guide for the language you choose to use - `PSR-2`, `gofmt`, etc.
- A git history (even if brief) with clear, concise commit messages.

---

Good luck!
