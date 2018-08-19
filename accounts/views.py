from django.shortcuts import render
from django import views
from django.http import request
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
import requests
from .forms import CustomUserCreationForm
from . import git


class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    template_name='signup.html'
    success_url=reverse_lazy('login')


  
def github_repos(request):
    user={}
    repos=[]
    if request.user.is_authenticated:

        if 'username' in request.GET:
            username=request.GET['username']
            user=git.user_profile(username)
            repos=git.user_repos(username)
            print(user)
    return render(request,'home.html',{
        'user':user,
        'repos':repos,
        })


def github_repo_commits(request):
    commits=[]
    username1=request.GET['username1']
    repo=request.GET['repo']

    print(repo)
    commits=git.user_commit_history(username1,repo)
    return render(request,'commits.html',{'commits':commits})


    