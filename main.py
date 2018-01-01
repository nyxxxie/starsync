import os
import git
import json
import tqdm
import requests

OUT_DIR='repos'
os.makedirs(OUT_DIR, exist_ok=True)


print('Fetching repo list.')
repos = []
for i in range(1, 100000):
    r = requests.get("https://api.github.com/users/nyxxxie/starred?page=" + i)
    j = json.loads(r.text)
    if len(j) == 0:
        break

    for repo in j:
        if repo['private']:
            continue
        repos.append(repo["html_url"])

print('Cloning {} repositories.'.format(len(repos)))
for repo in tqdm.tqdm(repos):
    git.Git(OUT_DIR).clone(repo)
