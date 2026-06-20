from prompt_craft import PromptCraft, PromptTemplate, UI, Database
import unittest
from unittest.mock import patch

class TestPromptCraft(unittest.TestCase):
    def test_add_template(self):
        prompt_craft = PromptCraft()
        template = PromptTemplate(1, "Template 1", "This is template 1")
        prompt_craft.add_template(template)
        self.assertEqual(len(prompt_craft.get_templates()), 1)

    def test_delete_template(self):
        prompt_craft = PromptCraft()
        template1 = PromptTemplate(1, "Template 1", "This is template 1")
        template2 = PromptTemplate(2, "Template 2", "This is template 2")
        prompt_craft.add_template(template1)
        prompt_craft.add_template(template2)
        prompt_craft.delete_template(1)
        self.assertEqual(len(prompt_craft.get_templates()), 1)

    def test_delete_template_api(self):
        prompt_craft = PromptCraft()
        template = PromptTemplate(1, "Template 1", "This is template 1")
        prompt_craft.add_template(template)
        self.assertEqual(prompt_craft.delete_template_api(1), 204)

    def test_delete_template_api_failure(self):
        prompt_craft = PromptCraft()
        self.assertEqual(prompt_craft.delete_template_api(1), 500)

    @patch('builtins.input', return_value='y')
    def test_ui_delete_template(self, mock_input):
        prompt_craft = PromptCraft()
        ui = UI(prompt_craft)
        template = PromptTemplate(1, "Template 1", "This is template 1")
        prompt_craft.add_template(template)
        ui.delete_template(1)
        self.assertEqual(len(prompt_craft.get_templates()), 0)

    def test_database_add_template(self):
        db = Database()
        template = PromptTemplate(1, "Template 1", "This is template 1")
        db.add_template(template)
        self.assertEqual(len(db.get_templates()), 1)

    def test_database_delete_template(self):
        db = Database()
        template1 = PromptTemplate(1, "Template 1", "This is template 1")
        template2 = PromptTemplate(2, "Template 2", "This is template 2")
        db.add_template(template1)
        db.add_template(template2)
        db.delete_template(1)
        self.assertEqual(len(db.get_templates()), 1)

if __name__ == '__main__':
    unittest.main()
