import pytest
from prompt_craft import PromptCraft, Commit
from datetime import datetime

@pytest.fixture
def prompt_craft():
    return PromptCraft()

def test_add_commit(prompt_craft):
    commit = Commit("1", datetime(2022, 1, 1), "John", "Hello World")
    prompt_craft.add_commit(commit)
    assert len(prompt_craft.get_commits()) == 1

def test_get_commits(prompt_craft):
    commit1 = Commit("1", datetime(2022, 1, 1), "John", "Hello World")
    commit2 = Commit("2", datetime(2022, 1, 2), "Jane", "Hello Universe")
    prompt_craft.add_commit(commit1)
    prompt_craft.add_commit(commit2)
    commits = prompt_craft.get_commits()
    assert len(commits) == 2
    assert commits[0].id == "1"
    assert commits[1].id == "2"

def test_get_diff(prompt_craft):
    commit1 = Commit("1", datetime(2022, 1, 1), "John", "Hello World")
    commit2 = Commit("2", datetime(2022, 1, 2), "Jane", "Hello Universe")
    diff = prompt_craft.get_diff(commit1, commit2)
    assert diff == "Diff between Hello World and Hello Universe"

def test_rollback(prompt_craft):
    commit1 = Commit("1", datetime(2022, 1, 1), "John", "Hello World")
    commit2 = Commit("2", datetime(2022, 1, 2), "Jane", "Hello Universe")
    prompt_craft.add_commit(commit1)
    prompt_craft.add_commit(commit2)
    prompt_craft.rollback(commit1)
    commits = prompt_craft.get_commits()
    assert len(commits) == 1
    assert commits[0].id == "1"

def test_get_history(prompt_craft):
    commit1 = Commit("1", datetime(2022, 1, 1), "John", "Hello World")
    commit2 = Commit("2", datetime(2022, 1, 2), "Jane", "Hello Universe")
    prompt_craft.add_commit(commit1)
    prompt_craft.add_commit(commit2)
    history = prompt_craft.get_history()
    assert len(history) == 2
    assert history[0]["id"] == "1"
    assert history[1]["id"] == "2"
