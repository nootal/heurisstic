#!/usr/bin/python

import os
import json
import sys

# Please download all repo stats before:
# wget https://api.github.com/search/repositories?q=repo:quarkslab/irma-ansible (this is just one repo)

repos = list()

for f in os.listdir("."):
    if not f.startswith("repo"):
        continue
    with open(f) as ff:
        j = json.load(ff)
        items = j["items"][0]
        repos.append(items)

def displayKey(r, key):
    print("\t{}: {}".format(key, r[key]))

watchers, forks, issues, stars = 0, 0, 0, 0
for r in repos:
    print(r["name"])
    displayKey(r,"pushed_at") 
    displayKey(r,"updated_at") 
    displayKey(r,"watchers_count")
    watchers += int(r["watchers_count"])
    displayKey(r,"stargazers_count") 
    stars += int(r["stargazers_count"])
    displayKey(r,"open_issues_count") 
    issues += int(r["open_issues_count"])
    displayKey(r,"forks_count") 
    forks += int(r["forks_count"])
print("watchers: {}".format(watchers))
print("forks: {}".format(forks))
print("issues: {}".format(issues))
print("stars: {}".format(stars))
