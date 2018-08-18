from django.shortcuts import render
import requests


def user_profile(username):
    user={}
    user_url='https://api.github.com/users/%s'% username   #url to the user profile
    response_user_url=requests.get(user_url)
    success_user_url=(response_user_url.status_code==200)
    user=response_user_url.json()
    user['success']=success_user_url
    return user


def user_repos(username):
    repos=[]
    repos_url='https://api.github.com/users/%s/repos'%username
    response_repos_url=requests.get(repos_url)
    success_repos_url=(response_repos_url.status_code==200)
    repos=response_repos_url.json()
    return repos

def user_commit_history(username,repo):
    commits=[]
    commits_url=f'https://api.github.com/repos/{username}/{repo}/commits'
    response_commits_url=requests.get(commits_url)
    success_commits_url=(response_commits_url.status_code==200)
    commits=response_commits_url.json()
    return commits
  
