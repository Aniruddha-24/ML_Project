# ML_project
This is first machine learning project

### Software and account Requirement.
### Github Account
### Heroku Account
### VS Code IDE
### GIT cli
### GIT Dontation

creating conda enviroment 
'''
conda create -p venv python==3.7 -y
'''

'''
conda activate venv/

OR

'''
conda activate venv
'''

'''
pip install -r requirements.txt
'''

To add files to git 
'''
git add .
'''
OR

'''
git add <file_name>
'''

Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
'''
git status
'''

To check all version maintained by git
'''
git log
'''


To create version/commit all changes by git 
'''
git commit -m "message"
'''

To send version/changes to github
'''
git push origin main
'''


To check remote url 
'''
git remote -v
'''


To setup CI/CD pipeline in heroku ew need 3 information

1. Heroku_Email = anivaze244@gmail.com
2. Heroku_API_Key = <>
3. Heroku_App_Name = aniruddha-app



Build docker image

'''
docker build -t <image_name>:<tagname>
'''

To list docker images

'''
docker images
'''

Run docker images

'''
docker run -p 5000:5000 -e PORT=5000 <image_id>
'''

To check running container in docker 

'''
docker ps
'''

To stop docker container 

'''
docker stop <container_id>
'''




