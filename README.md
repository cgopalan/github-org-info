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
Some endpoints require authentication. For that, specify your github user and password (or a generated password token) in the [config file] (app/settings_default.py)

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
