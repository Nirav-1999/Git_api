from django.conf.urls import url
from . import views


app_name='accounts'

urlpatterns = [
    url(r'^$',views.SignUpView.as_view(),name='signup'),
    url(r'^Git/$',views.github_repos,name='search'),
    url(r'^Git/commits/$',views.github_repo_commits,name='commits'),

   
]  