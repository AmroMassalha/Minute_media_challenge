# Minute Media - homework

The attached project have the solution of the homework assignment

## Installation

Useing [Python3.6 +](https://www.python.org/) and python packages Locust & Requests

```shell
pip install requests, pytest
```

###### API:

    in the API test we covered all request we found a bug in the service that the post users (create user) gets an integer ID as the documentation but the app requires it as a string.
    we have another problem that related to decoding I do not have a root cause for it, it seems to be a problem with my MAC (first time I face such errors, still looking for a solution)
    because of the failure of the post API the put and delete also not tested

    another bug we have - that when we pass an empty dict as a header in the post API the flask server accepts it as a None type

##### WEB:

    we have also created infra for the selenium task another problem we have that I did not manage to get a list of elements
