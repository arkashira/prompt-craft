import json
from dataclasses import dataclass
from typing import List

@dataclass
class PromptTemplate:
    id: int
    name: str
    content: str

class PromptCraft:
    def __init__(self):
        self.templates = []

    def add_template(self, template: PromptTemplate):
        self.templates.append(template)

    def delete_template(self, template_id: int):
        self.templates = [t for t in self.templates if t.id != template_id]

    def get_templates(self):
        return self.templates

    def delete_template_api(self, template_id: int):
        try:
            if not any(t.id == template_id for t in self.templates):
                raise Exception("Template not found")
            self.delete_template(template_id)
            return 204
        except Exception as e:
            return 500

class UI:
    def __init__(self, prompt_craft: PromptCraft):
        self.prompt_craft = prompt_craft

    def delete_template(self, template_id: int, confirm=True):
        if confirm:
            self.prompt_craft.delete_template(template_id)
            print("Template deleted successfully")
        else:
            print("Deletion cancelled")

class Database:
    def __init__(self):
        self.templates = []

    def add_template(self, template: PromptTemplate):
        self.templates.append(template)

    def delete_template(self, template_id: int):
        self.templates = [t for t in self.templates if t.id != template_id]

    def get_templates(self):
        return self.templates

def main():
    prompt_craft = PromptCraft()
    db = Database()
    ui = UI(prompt_craft)
    template1 = PromptTemplate(1, "Template 1", "This is template 1")
    template2 = PromptTemplate(2, "Template 2", "This is template 2")
    prompt_craft.add_template(template1)
    prompt_craft.add_template(template2)
    db.add_template(template1)
    db.add_template(template2)
    ui.delete_template(1)
    print("Remaining templates:")
    for template in prompt_craft.get_templates():
        print(template.name)

if __name__ == "__main__":
    main()
