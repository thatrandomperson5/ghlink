import os
from git import Repo

repo_path = os.getenv("GIT_REPO_PATH")

repo = Repo(repo_path)
assert repo.bare

print("Repo at {} successfully loaded.".format(repo_path))
print("Repo description: {}".format(repo.description))
print("Repo active branch is {}".format(repo.active_branch))
for remote in repo.remotes:
    print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
print("Last commit for repo is {}.".format(str(repo.head.commit.hexsha)))
