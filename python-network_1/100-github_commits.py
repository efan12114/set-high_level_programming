#!/usr/bin/python3
"""Lists 10 most recent commits of a repository by an owner"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    try:
        commits = r.json()
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    except Exception:
        pass
