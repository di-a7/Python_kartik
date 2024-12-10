<!-- # git commands -->

<!-- # [to initialize git repo] -->
git init 

<!-- add the specific file to the staging area                     -->
git add <file name>           [to add single file to staging area]

<!-- <add the all file to the staging area> -->
git add .                     [to add multiple or all files to staging area]

<!-- <to add messages to the commits> -->
git commit -m "Your messages"

<!-- <change the name of default branch from master to main> -->
git branch -M main

<!-- <create a new branch> -->
git branch branch_name

<!-- <to check the number of branches> -->
git branch

<!-- <to merge branches> -->
git merge branch_name

<!-- <to change the branch eg. from main branch to ram branch> -->
git checkout your_branch_name


git remote add origin <name of your git repo>

<!-- to push into github -->
git push -u origin <branch_name>

<!-- <to update your remot repo according to the changes made in local repo> -->
git push

<!-- <to update your local repo according to the changes made in remote repo> -->
git pull

sfseger
this is git file, this is the changes