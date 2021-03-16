import unittest
import HW04a
from HW04a import github_repos_commits, Repos, Commits
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none, assert_list_equal

class test_commits(unittest.TestCase):
    @Mock('requests.get')
    def test_Commits(self, mockedReq):
        mockedReq.return_value = True
        commits = Commits(self.username, self.repo_name)
        self.assert_Equal(commits, True)

