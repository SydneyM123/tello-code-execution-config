from git import Repo

repo = Repo("./public/")
origin = repo.remotes.origin
origin.fetch()
diff = repo.git.diff("master..remotes/origin/master", name_only=True)
print("Changed files: ")
print(diff)
origin.pull()
