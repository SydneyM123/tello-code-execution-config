from git import Repo

repo = Repo(".")

for remote in repo.remotes:
    remote.fetch()

diff = repo.git.diff("HEAD..remotes/origin/HEAD", name_only=True)

print(diff)