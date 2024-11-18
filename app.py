from ghapi.all import GhApi
import pytest

def get_repo_info(owner, repo):
    api = GhApi()
    return api.repos.get(owner, repo)

def test_get_repo_info():
    owner = "octocat"
    repo = "Hello-World"
    repo_info = get_repo_info(owner, repo)
    assert repo_info.name == repo
    assert repo_info.owner.login == owner

if __name__ == "__main__":
    owner = "octocat"
    repo = "Hello-World"
    info = get_repo_info(owner, repo)
    print(f"Repository: {info.name}, Owner: {info.owner.login}")
