# Connor Smith
# Professor Saremi
# SSW 567
# HW 04a
# "I pledge my honor that I have abided by the Stevens Honor System"

# import library
import requests

# request user inputted GitHub ID
user_id = input("Please enter your GitHub ID: ")

# create function to find both repos and number of commits
def github_repos_commits(user_id):
    repos = Repos(user_id)
    output = {}
    for repo in repos:
        repo_name = repo["name"]
        output[repo_name] = Commits(user_id, repo_name)
    print(output)
    return output

# create function to find repos
def Repos(user_id):
    r = requests.get("https://api.github.com/users/" + user_id + "/repos")
    data = r.json()
    return data

# create function to find number of commits per repo
def Commits(user_id, repo_name):
    r = requests.get("https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits")
    data = r.json()
    return "Number of commits: ", len(data)

github_repos_commits(user_id)