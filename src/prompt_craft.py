import argparse
import json
import sys
from dataclasses import dataclass

@dataclass
class Template:
    id: int
    title: str
    version: str

class PromptCraft:
    def __init__(self, api_token):
        self.api_token = api_token
        self.templates = []

    def list_templates(self):
        # Simulate API call to get templates
        self.templates = [
            Template(1, "Template 1", "1.0"),
            Template(2, "Template 2", "2.0"),
        ]
        return self.templates

    def to_json(self):
        return json.dumps([{"id": t.id, "title": t.title, "version": t.version} for t in self.templates])

def main():
    parser = argparse.ArgumentParser(description="Prompt Craft CLI")
    parser.add_argument("command", choices=["list"])
    parser.add_argument("--api-token", required=True)
    args = parser.parse_args()
    craft = PromptCraft(args.api_token)
    if args.command == "list":
        try:
            templates = craft.list_templates()
            print(craft.to_json())
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
