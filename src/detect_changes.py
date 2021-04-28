from git import Repo


repo = Repo("./public/")
repo.git.fetch("origin", "master")

diff = repo.git.diff("--name-only", "-- '***.py'")

print("Changed files: ")
print(diff)

repo.git.pull("origin", "master")
