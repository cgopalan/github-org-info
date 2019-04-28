"""
    Helper functions that either provide utility functions or help in generating
    information for the endpoints in routes file.
"""

import requests
from flask import current_app as app
from flask import jsonify

from .results import GithubResults
from .retry import RetryError

GITHUB_URL_PREFIX = 'https://api.github.com/orgs'
BITBUCKET_URL_PREFIX = 'https://api.github.com/orgs'
RECORDS_PER_PAGE=100
RETRY_ERROR_CODES = [408, 502, 503, 504]
RETRY_COUNT = 3

def get_github_profile(name):
    """ Gets profile information from github. Returns None if no data found.
        #TODO: Need to apply the retry decorator to this method.
    """
    try:
        resp = requests.get("{}/{}".format(GITHUB_URL_PREFIX, name), auth=(app.config['USER'], app.config['PASSWORD']))
        resp.raise_for_status()
        # Get Repos
        org_json = resp.json()
        output_results = []
        resp = requests.get("{}?per_page={}".format(org_json['repos_url'], RECORDS_PER_PAGE),
                            auth=(app.config['USER'], app.config['PASSWORD']))
        resp.raise_for_status()
        output_results.extend(resp.json())
        while 'next' in resp.links:
            resp = requests.get(resp.links['next']['url'],
                            auth=(app.config['USER'], app.config['PASSWORD']))
            resp.raise_for_status()
            output_results.extend(resp.json())
        ghr = GithubResults(org_json, output_results)
        return ghr.result
    except requests.exceptions.HTTPError as e:
        if e.response.status_code in RETRY_ERROR_CODES:
            raise RetryError
        elif e.response.status_code == 404:
            raise OrgNotFoundError


def get_bitbucket_team():
    """ To be implemented. """
    #raise Exception
    return {"bitbucket": "Not Implemented Yet"}


def merge_info(gh_org, bbt_team):
    """ Merges github profile and bitbucket team info.
        Currently only returns github info.
    """
    return gh_org


def build_response(response_template, status=None, message=None, result=None):
    """ Builds the complete response json to be returned to clients. """
    response_template["status"] = status
    response_template["message"] = message
    response_template["result"] = result
    return jsonify(response_template)

class OrgNotFoundError(Exception):
    """ Models an error denoting missing github organization. """
    pass
