# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

You can use a virtual environment (conda, venv, etc):
```
conda env create -f environment.yml
source activate user-profiles
```

Or just pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"
```

#### Authentication
Some endpoints require authentication. For that, specify your github user and password (or a generated password token) in the [config file](app/settings_default.py)

#### Endpoints
For a list of endpoints, check out the [API documentation](apidocs.md)


## Running tests

You can run tests just using the unittest module in the standard library
```
python -m unittest -v
```
Or you can run it via pytest.

Install pytest:
```
pip install pytest
```
Then run:
```
pytest -v
```


## What'd I'd like to improve on...

- Could not implement the bitbucket portion due to lack of time.
- If there were more endpoints, I would use a library like Flask-RESTFul which offers more functionality out of the box.
- Logging is currently done to the console. Logs need to persist to a file for monitoring and analysis.
- The retry functionality is incomplete. Although thats the design I would choose to go with.
- Tests should be in their own separate directory, but putting them there needed some munging around with file paths, so I put them in the app directory for now.
- Need to add more unit tests.
- Need to add integration tests.
- I chose to return null in the response for some values that were empty. Other choices would be to return empty strings or not include the property at all.
I think including them is better, since it keeps the response body consistent. I do not have a strong opinion on whether it should be null or empty string.
I guess it depends on the use case, and how our clients choose to process the data that they get from the api.

All in all, I had great fun working on this. Thanks!