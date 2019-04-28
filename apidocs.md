# API Documentation

These are the endpoints that are available.


## `GET /api/health-check`

A health check to see if the API is up and running.


## `GET /api/v1/profiles/:name`

Get the github profile for the organization. (In future will also get bitbucket info and merge the information)

##### PARAMS:

*  **`name`** - The name of the github organization

##### RESPONSE:

*  **`status`** - The status of the call. If it succeeds, it returns "success". Otherwise "error".
*  **`message`** - The message returned. Returns "No records found" when there are no records, and the error message if there is an error.
*  **`result`** - The result json that is returned when there are no errors. If there are errors, this will be null.