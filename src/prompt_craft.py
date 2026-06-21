import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Commit:
    id: str
    timestamp: datetime
    author: str
    prompt: str

class PromptCraft:
    def __init__(self):
        self.commits = []

    def add_commit(self, commit: Commit):
        self.commits.append(commit)

    def get_commits(self) -> List[Commit]:
        return self.commits

    def get_diff(self, commit1: Commit, commit2: Commit) -> str:
        return f"Diff between {commit1.prompt} and {commit2.prompt}"

    def rollback(self, commit: Commit):
        self.commits = [c for c in self.commits if c.timestamp <= commit.timestamp]

    def get_history(self) -> List[dict]:
        return [{"id": c.id, "timestamp": c.timestamp, "author": c.author, "prompt": c.prompt} for c in self.commits]
