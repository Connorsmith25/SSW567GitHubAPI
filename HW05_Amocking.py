from unittest import mock
from HW04a import github_repos_commits, Repos, Commits

@mock.patch('requests.get')
def TestGithubAPI (self, MockedReq):
    MockedReq.return_value = '[{"connorsmith25": 1}, {"connorsmith25": 2},{ "connorsmith25": 3},{ "connorsmith25": 4},{ "connorsmith25": 5},{ "connorsmith25": 6}'
    commits = Commits(self.user_id, self.repo_name)
    self.assertEqual(len(commits), 6)