import logging

import flask
from flask import Response, jsonify
import requests
from .helper import get_github_profile, get_bitbucket_team, merge_info, build_response


app = flask.Flask("user_profiles_api")
app.config.from_object('app.settings_default')
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)

@app.route("/api/v1/profile/<name>")
def get_profile(name):
    """
    Gets the merged bitbucket team and github org profile.
    If we get an error on either, send an error response json to client.
    """
    # Response json high-level structure
    response_template = {"status":  None,
                         "message": None,
                         "result":    None}
    # Try getting github info
    try:
        gho = get_github_profile(name)
    except Exception as e:
        app.logger.error(f"Could not fetch data from github. Error was: {e}")
        return build_response(response_template, status="error", message="Could not fetch data from github")

    # Now try bitbucket
    try:
        bbt = get_bitbucket_team()
    except Exception as e:
        app.logger.error(f"Could not fetch data from bitbucket. Error was: {e}")
        return build_response(response_template, status="error", message="Could not fetch data from bitbucket")

    # Check if the org or team exists. Send a message back if no info found.
    if not gho and not bbt:
        return build_response(response_template, status="success", message="No records found for profile")

    # At least one of bitbucket or github info was found
    return build_response(response_template, status="success", result=merge_info(gho, bbt))
