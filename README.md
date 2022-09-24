
# Skills 2022 test

## Task1:
### Task name: 
Manage GitHub scripts and documents
### Task preparation: 
create `Skills2022` directory inside the home directory using `mkdir` 
### Task implementation 
 1. Create `Skills2022` directory![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/1.png)
 2. Initialize the local repository, Create `README.md` file and add it to the repo. ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/2.png)
 3. Create remote repo and add remote origin ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/3.png)
 4. Had the error  `Password support removed` and solve it using the following commands after create personal access token (explained in details in task troubleshooting).
 5. push the commits to the remote repo using `push` command ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/4.png)
### Task troubleshooting 
We can create access token from your GitHub account, go to **Settings** => **Developer Settings** => **Personal Access Token** => **Generate New Token** (Give your password) => **Fillup the form** => click **Generate token** => **Copy the generated Token**![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/problem-solve-1.png)
then use the following commands as in the step5 screenshot 
```
$ git config --global user.name "your_github_username"
$ git config --global user.email "your_github_email"
$ git config -l
```
### Task verification 
![=> proof of the quality of the result (Screenshots)(Task1Screens)](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/4.png)
