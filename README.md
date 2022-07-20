#currently working

# Machine-Learning-project1
My First Machine Learning Project

# Software and account Requirements:

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

create conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```
TO add files in git
```
git add .
```
OR
```
git add <filename>
```
To see the status
```
git status
```
> Note : To ignore the specific file/folder from git we can add the name in the .gitignore file.

To check git version maintained
```
git log
```

To create version/commit all change by git
```
git commit -m "message"
```

To send version/changes to github
```
git push main origin
```

To check remote URL
```
git remote -v
```

To check Push and Pull Branch
```
git branch
```

To see the difference from the previous file
```
git diff
```

To setup CI/CD pipeline in heroku we need three informations:

1. Heroku_Email_ID = <>
2. Heroku_API_Key  = <>
3. Heroku_APP_Name  = <>

Build Docker Image
```
docker build -t <imagename>:<tagname> .
```
> NOTE: the letters in docker image name  should be always lowercase

To list docker_images
```
docker images
```

To run docker Images
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
```
To check the running container in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```
to install jupyter Notebook in vscode
```
pip install ipykernel
```
