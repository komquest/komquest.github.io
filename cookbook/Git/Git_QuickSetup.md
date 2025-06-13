# Restore Old Code and Recommit:

```
cd ~/git/your-repo-root
git log
# find the commit id you want
git checkout <commitId> . 
# IMPORTANT NOTE: the trailing `.` in the previous line is important!
git commit -m "Restoring old source code"

```


# Easy Git Config Guide:

https://rogerdudler.github.io/git-guide/


# Git Push with Token

```
git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git
```