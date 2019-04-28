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

### Making Requests

Check out the [API documentation](apidocs.md)
```
curl -i "http://127.0.0.1:5000/health-check"
```


## What'd I'd like to improve on...
