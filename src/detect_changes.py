from git import Repo

repo = Repo(".")

diff = repo.git.diff("master..remotes/origin/master",name_only=True)
print(diff)