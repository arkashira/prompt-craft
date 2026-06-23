import json
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

@dataclass
class PromptTemplate:
    id: str
    title: str
    description: str
    prompt_body: str
    created_at: str

class PromptCraft:
    def __init__(self):
        self.templates = {}

    def create_template(self, title, description, prompt_body):
        if not title:
            raise ValueError("Title cannot be empty")
        if not description:
            raise ValueError("Description cannot be empty")
        if not prompt_body:
            raise ValueError("Prompt body cannot be empty")

        template_id = str(uuid4())
        template = PromptTemplate(
            id=template_id,
            title=title,
            description=description,
            prompt_body=prompt_body,
            created_at=datetime.now().isoformat()
        )
        self.templates[template_id] = template
        return template

    def get_template(self, template_id):
        return self.templates.get(template_id)

    def list_templates(self):
        return list(self.templates.values())
