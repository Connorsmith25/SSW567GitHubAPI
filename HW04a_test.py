import unittest
from HW04a import github_repos_commits, Repos, Commits, user_id
repo_test = "hellogitworld"

class TestHW04a(unittest.TestCase):
    def test_repos(self):
        self.assertGreater(len(github_repos_commits(user_id)), 0)
        self.assertLess(len(github_repos_commits(user_id)), 1000)
        self.assertGreater(len(github_repos_commits(user_id)), 0)

    def test_Commits(self):
        self.assertGreater(len(Commits(user_id, repo_test)), 0)
        self.assertLess(len(Commits(user_id, repo_test)), 1000)

if __name__ == '__main__':
    unittest.main()