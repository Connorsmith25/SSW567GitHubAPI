# Connor Smith
# Professor Saremi
# SSW 567
# HW 04a
# "I pledge my honor that I have abided by the Stevens Honor System"

# import library
import requests

# Greet user and request user inputted GitHub ID & specific repo name if required
#print("Hi, this program will show the number of commits for given GitHub repos for a GitHub user.")
#user_id = input("Please enter your GitHub ID: ")
#repo_id = input("Please enter your repo name (if you want to see all repos for this user, enter 'NA'): ")


# create function to find both repos and number of commits as well as number of repos by using a count function
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


#if repo_id == 'NA':
    #github_repos_commits(user_id)
#else:
    #Commits(user_id, repo_id)
