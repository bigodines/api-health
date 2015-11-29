# api-health
[![Build Status](https://travis-ci.org/bigodines/api-health.svg)](https://travis-ci.org/bigodines/api-health)
```
Disclaimer:

API-Health is still under heavily development. If you are planning on using it for anything else than playing around,
please consider dropping me a line so I start caring about backwards compatibility.
```

## Quickstart

#### setup
* clone this repo
* pip install -r requirements.txt
* python manage.py test
* python manage.py runserver

#### using (via api)
>###### get all tasks

```bash
curl "http://localhost:8080/api/task"
```

>##### create a task

Creating a new task is as simple as making a POST request to /api/task with a URL and a list (comma separated) of required fields

```bash
curl "http://localhost:8080/api/task" -X POST -d '{"url":"http://api.github.com", "expected_fields": "current_user_url" }'
```

>##### update a task

Same as "create", but we'll use **PUT** and also the _id_ field is required.
```bash
curl "http://localhost:8080/api/task" -X PUT -d '{"id": 1, "url":"http://api.github.com", "expected_fields": "current_user_url" }'
```

>##### deletion

Send a **DELETE** call with the task _id_

```bash
curl "http://localhost:8080/api/task?id=1" -X DELETE
```

>##### execute tasks

There are two ways to run tasks. It can be done by running **cronjob.py** or by a rest call to /run:
```bash
curl "http://localhost:8080/api/run"
```

## Introduction
API-Health  started as a pet project to refresh my mind after 5 years without coding in Python. I wanted to make something useful, thus I've decided to create an automatic way to monitor when APIs break their contract (or purpose or due to bugs).

The **how** we'll achieve this is really open and full of experiments. It started from a cookie-cutter template that used _bottle_, which has been replaced by _tornado_ due to the amazing coroutines and built-in queue management.

### Roadmap
* The initial plan is to create a solid API that enables developers to hook **api-health** to their existing CI/CD pipelines.
* I also wanna play with a few frontend-y stack. I've already started something but will revisit the whole thing, I realize that in order to get people using it, I'll probably have to add ```insert a javascript buzzword framework here```.
* The system must be **very** flexible (which it is not, as of today) and the worker/queue must be very efficient.
* We are gonna build a dashboard to measure the most important open APIs on the internets! ;P

### Get involved
I'm so happy that you wanna play with me! Here are the simple rules of this project:
* No PR will be merged without tests.
* Commit messages should look **beautiful** when read on **tig** (this means: avoid one-liner messages)
* Use "issues"  to track/add features so we don't work on the same stuff :)

### License
MIT.
