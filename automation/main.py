#!/bin/env python3

import requests
from pyrpm.spec import Spec
from packaging import version
from git.repo import Repo


API = "https://api.github.com"
SPEC="vale.spec"
SPEC_PATH=f"../{SPEC}"

def get_latest_version() -> str:
    owner = "errata-ai"
    repo = "vale"
    releases_url = f"{API}/repos/{owner}/{repo}/releases/latest"

    return requests.get(releases_url).json()["tag_name"][1:]


def get_package_version() -> str:
    return Spec.from_file(SPEC_PATH).version


def update_version() -> bool:
    latest_v = get_latest_version()
    current_v = get_package_version()

    if version.parse(latest_v) > version.parse(current_v):
        spec_file_content: str
        with open(SPEC_PATH, "rt") as f:
            spec_file_content = f.read()

        spec_file_content = spec_file_content.replace(current_v, latest_v, 1)

        with open(SPEC_PATH, "wt") as f:
            f.write(spec_file_content)
        return True

    return False


def commit_changes():
    repo = Repo('..')

    if repo.active_branch.name != "main":
        repo.heads.main.checkout()
    
    repo.index.add([SPEC])
    repo.index.commit("feat: Update package version")
    # repo.remotes[0].push()


if __name__ == '__main__':
    if update_version():
        commit_changes()
