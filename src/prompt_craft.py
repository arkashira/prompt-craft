import json
from dataclasses import dataclass
from typing import List

@dataclass
class Project:
    name: str
    prompts: List[str]

@dataclass
class User:
    email: str
    projects: List[Project]

class PromptCraft:
    def __init__(self):
        self.users = {}
        self.free_tier_limits = {"projects": 5, "eval_calls": 10000}

    def create_project(self, user_email, project_name):
        if user_email not in self.users:
            self.users[user_email] = User(email=user_email, projects=[])
        if len(self.users[user_email].projects) >= self.free_tier_limits["projects"]:
            raise ValueError("Free tier project limit reached")
        self.users[user_email].projects.append(Project(name=project_name, prompts=[]))
        return self.users[user_email].projects[-1]

    def edit_prompt(self, user_email, project_name, prompt):
        if user_email not in self.users:
            raise ValueError("User not found")
        for project in self.users[user_email].projects:
            if project.name == project_name:
                project.prompts.append(prompt)
                return project
        raise ValueError("Project not found")

    def run_evaluation(self, user_email, project_name):
        if user_email not in self.users:
            raise ValueError("User not found")
        for project in self.users[user_email].projects:
            if project.name == project_name:
                # Simulate evaluation
                return {"result": "success"}
        raise ValueError("Project not found")

    def send_welcome_email(self, user_email):
        # Simulate sending email
        return {"message": "Welcome email sent"}

    def get_free_tier_limits(self):
        return self.free_tier_limits
