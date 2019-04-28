import unittest
from .results import GithubResults
from .testdata import TEST_ORG_DATA, TEST_REPO_DATA

class GitHubResultsTest(unittest.TestCase):
    
    def setUp(self):
        self.ghr = GithubResults(TEST_ORG_DATA, TEST_REPO_DATA)

    def test_get_total_repo_count(self):
        self.assertEqual(297, self.ghr.get_total_repo_count())

    def test_get_watcher_count(self):
        self.assertEqual(1042, self.ghr.get_watcher_count())

    def test_get_original_repo_count(self):
        self.assertEqual(2, self.ghr.get_original_repo_count())

    def test_get_forked_repo_count(self):
        self.assertEqual(1, self.ghr.get_forked_repo_count())

    def test_get_languages_info(self):
        lang_count, langs = self.ghr.get_languages_info()
        self.assertEqual(2, lang_count)
        self.assertEqual({"Ruby", "Python"}, set(langs))

if __name__ == '__main__':
    unittest.main()
