import unittest
from unittest.mock import Mock, MagicMock
import requests

def github_repos_commits(username):
    repos = Repos(username)
    output = {}
    count = 0
    for repo in repos:
        count = count + 1
        repo_name = repo["name"]
        output[repo_name] = Commits(username, repo_name)
    print("Total number of repos for this user:", count)
    return output


# create function to find repos
def Repos(username):
    r = requests.get("https://api.github.com/users/" + username + "/repos")
    data = r.json()
    return data


# create function to find number of commits per repo
def Commits(username, repo_name):
    r = requests.get("https://api.github.com/repos/" + username + "/" + repo_name + "/commits")
    data = r.json()
    print("Number of commits for",repo_name,":",len(data))
    return len(data)

@Mock('requests.get')
def test_Commits(self, mockedReq):
    mockedReq.return_value = MagicMock('MockSuccess')
    commits = Commits(self.username, self.repo_name)
    self.assertEqual(commits, 'MockSuccess')
