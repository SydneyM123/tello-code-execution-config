from git import Repo

repo = Repo("./public/")

for remote in repo.remotes:
    remote.fetch()

diff = repo.git.diff("master..remotes/origin/master", name_only=True)

print("Changed files: ")
print(diff)

for remote in repo.remotes:
    try:    
        remote.pull()
    except Exception as e:
        print(e)
