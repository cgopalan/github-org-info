# API Documentation

These are the endpoints that are available.


## `GET /health-check`

A health check to see if the API is up and running.

##### Requires Authentication: No

##### PARAMS: None

##### RESPONSE: All Good!


## `GET /api/v1/profiles/:name`

Get the github profile for the organization. (In future will also get bitbucket info and merge the information)

##### Requires Authentication: Yes

##### PARAMS:

*  **`name`** - The name of the github organization

##### RESPONSE:

*  **`status`** - The status of the call. If it succeeds, it returns "success". Otherwise "error". Error may denote a client error or server error.
*  **`message`** - The message returned. Returns "No records found" when there are no records, and a concise error message if there is an error.
*  **`result`** - The result json that is returned when there are no errors. If there are errors, this will be null.