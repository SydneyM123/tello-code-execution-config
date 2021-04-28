from git import Repo


repo = Repo("./public/")
repo.git.fetch("origin", "master")
diff = repo.git.diff("master..remotes/origin/master", name_only=True)
print("Changed files: ")
print(diff)
repo.git.pull("origin", "master")
