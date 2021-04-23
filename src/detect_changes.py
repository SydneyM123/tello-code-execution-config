from git import Repo

repo = Repo(".")

diff = repo.git.diff("master..remotes/origin/master",name_only=True)
print(diff)
diff = repo.git.diff(name_only=True)
print(diff)