import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Template:
    id: int
    name: str
    content: str

class TemplateService:
    def __init__(self):
        self.templates = []
        self.id_counter = 0

    def create_template(self, name: str, content: str) -> Template:
        self.id_counter += 1
        template = Template(self.id_counter, name, content)
        self.templates.append(template)
        return template

    def get_template(self, id: int) -> Template:
        for template in self.templates:
            if template.id == id:
                return template
        raise ValueError("Template not found")

class AuthService:
    def __init__(self):
        self.tokens = {}

    def generate_token(self, user: str) -> str:
        token = f"token-{user}"
        self.tokens[token] = user
        return token

    def verify_token(self, token: str) -> bool:
        return token in self.tokens

class RateLimiter:
    def __init__(self):
        self.requests = {}

    def is_allowed(self, ip: str) -> bool:
        if ip not in self.requests:
            self.requests[ip] = 0
        self.requests[ip] += 1
        return self.requests[ip] <= 10

class API:
    def __init__(self):
        self.template_service = TemplateService()
        self.auth_service = AuthService()
        self.rate_limiter = RateLimiter()

    def create_template(self, token: str, name: str, content: str) -> Dict:
        if not self.auth_service.verify_token(token):
            raise ValueError("Invalid token")
        if not self.rate_limiter.is_allowed("localhost"):
            raise ValueError("Rate limit exceeded")
        template = self.template_service.create_template(name, content)
        return {"id": template.id, "name": template.name, "content": template.content}

    def get_template(self, token: str, id: int) -> Dict:
        if not self.auth_service.verify_token(token):
            raise ValueError("Invalid token")
        template = self.template_service.get_template(id)
        return {"id": template.id, "name": template.name, "content": template.content}
