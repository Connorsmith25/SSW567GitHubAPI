import unittest
from HW04a import github_repos_commits, Repos, Commits

class TestHW04a(unittest.TestCase):

    def test_Commits(self):
        self.assertEqual((Commits("richkempinski", "hellogitworld")), 30)
        self.assertEqual((Commits("Connorsmith25", "SSW567")), 3)

if __name__ == '__main__':
    unittest.main()