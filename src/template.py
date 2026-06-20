import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class Template:
    id: int
    name: str
    content: str

class TemplateService:
    def __init__(self):
        self.templates = {}
        self.next_id = 1
        self.rate_limit = 5  # requests per minute
        self.rate_limit_window = timedelta(minutes=1)
        self.request_timestamps = {}

    def create_template(self, user_id: int, template: Dict[str, str]) -> Template:
        if user_id not in self.request_timestamps:
            self.request_timestamps[user_id] = []
        now = datetime.now()
        self.request_timestamps[user_id] = [ts for ts in self.request_timestamps[user_id] if now - ts < self.rate_limit_window]
        if len(self.request_timestamps[user_id]) >= self.rate_limit:
            raise Exception("Rate limit exceeded")
        self.request_timestamps[user_id].append(now)
        template_id = self.next_id
        self.next_id += 1
        self.templates[template_id] = Template(template_id, template["name"], template["content"])
        return self.templates[template_id]

    def authenticate(self, token: str) -> int:
        # Simple JWT authentication for demonstration purposes
        if token == "secret_token":
            return 1
        raise Exception("Invalid token")

class API:
    def __init__(self):
        self.template_service = TemplateService()

    def handle_post(self, token: str, template: Dict[str, str]) -> Dict[str, str]:
        user_id = self.template_service.authenticate(token)
        template = self.template_service.create_template(user_id, template)
        return {"id": template.id, "name": template.name, "content": template.content}
