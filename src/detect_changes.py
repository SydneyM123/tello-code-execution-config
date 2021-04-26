from git import Repo

repo = Repo("/public/")

for remote in repo.remotes:
    print(remote)
    remote.fetch()

diff = repo.git.diff("HEAD..remotes/origin/HEAD", name_only=True)

print(diff)
