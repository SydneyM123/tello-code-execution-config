from git import Repo


repo = Repo("./public/")
repo.git.fetch("origin", "master")

diff = repo.git.diff(name_only=True, "-- *.py", "master..remotes/origin/master")
print("Changed files: ")
print(diff)

repo.git.pull("origin", "master")
