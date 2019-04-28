"""
    Model classes that encapsulate results fetched from sources.
    The code to transform data and compute aggregates and other results
    needed by the client should be here.
"""

class GithubResults:
    
    def __init__(self, org_dict, repos_dict):
        self.org_dict = org_dict
        self.repos_dict = repos_dict
    
    @property
    def result(self):
        result_template = {
            "public_repos" : { "total": 100, "original": 45, "forked": 55},
            "watchers_count": 34,
            "languages": {"total": 23, "members": []},
            }
        result_template['public_repos']['total'] = self.get_total_repo_count()
        result_template['public_repos']['original'] = self.get_original_repo_count()
        result_template['public_repos']['forked'] = self.get_forked_repo_count()
        result_template['watchers_count'] = self.get_watcher_count()
        result_template['languages']['total'], result_template['languages']['members'] = self.get_languages_info()
        return result_template

    def get_total_repo_count(self):
        return self.org_dict["public_repos"]

    def get_watcher_count(self):
        return sum(x['watchers_count'] for x in self.repos_dict)
    
    def get_original_repo_count(self):
        return sum(1 for x in self.repos_dict if not x['fork'])
    
    def get_forked_repo_count(self):
        return sum(1 for x in self.repos_dict if x['fork'])
    
    def get_languages_info(self):
        langs = {x['language'] for x in self.repos_dict if x['language']}
        # Need to convert set to list to make it JSON serializable
        return len(langs), list(langs)
    
    def get_topics_info(self):
        """ To be implemented. """
        pass


class BitbucketResults:
    pass
