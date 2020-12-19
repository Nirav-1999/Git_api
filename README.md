Git Api

Introduction
This project uses github api to to search for a user ,his/her repos and also the commit histories of a particular repo. 

Details
The app named accounts helps user to log in and search for user accounts(github accounts). 
For login and signup I have created custom user creation forms in forms.py  using djangos inbuilt base classes. 
The file git.py consists of all the functions to get the corresponding json file from the api. 
Views.py uses this git.py file and displays the required templates when it is called by urls.py file

![picture](https://bitbucket.org/Nirav-jain/git_api/raw/master/Screenshots/Login.png)


![picture](https://bitbucket.org/Nirav-jain/git_api/raw/master/Screenshots/SignUp.png)

When a user logs in the following screen appears:
 
![picture](https://bitbucket.org/Nirav-jain/git_api/raw/master/Screenshots/FirstPage.png)
On searching the username
![picture](https://github.com/Nirav-1999/Git_api/tree/master/Screenshots/AfterSearch.png)


On clicking View commit history:
 
 
![picture](https://bitbucket.org/Nirav-jain/git_api/raw/master/Screenshots/CommitHistory1.png)

![picture](https://bitbucket.org/Nirav-jain/git_api/raw/master/Screenshots/CommitHistory2.png)



 
 
 
 



