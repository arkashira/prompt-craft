import pytest
from src.prompt_craft import PromptCraft, PromptTemplate

@pytest.fixture
def prompt_craft():
    return PromptCraft()

def test_create_template(prompt_craft):
    title = "Test Title"
    description = "Test Description"
    prompt_body = "Test Prompt Body"
    template = prompt_craft.create_template(title, description, prompt_body)
    assert isinstance(template, PromptTemplate)
    assert template.title == title
    assert template.description == description
    assert template.prompt_body == prompt_body
    assert template.id in prompt_craft.templates

def test_get_template(prompt_craft):
    title = "Test Title"
    description = "Test Description"
    prompt_body = "Test Prompt Body"
    template = prompt_craft.create_template(title, description, prompt_body)
    retrieved_template = prompt_craft.get_template(template.id)
    assert retrieved_template == template

def test_list_templates(prompt_craft):
    title1 = "Test Title 1"
    description1 = "Test Description 1"
    prompt_body1 = "Test Prompt Body 1"
    template1 = prompt_craft.create_template(title1, description1, prompt_body1)
    title2 = "Test Title 2"
    description2 = "Test Description 2"
    prompt_body2 = "Test Prompt Body 2"
    template2 = prompt_craft.create_template(title2, description2, prompt_body2)
    templates = prompt_craft.list_templates()
    assert len(templates) == 2
    assert template1 in templates
    assert template2 in templates

def test_create_template_with_empty_title(prompt_craft):
    with pytest.raises(ValueError):
        prompt_craft.create_template("", "Test Description", "Test Prompt Body")

def test_create_template_with_empty_description(prompt_craft):
    with pytest.raises(ValueError):
        prompt_craft.create_template("Test Title", "", "Test Prompt Body")

def test_create_template_with_empty_prompt_body(prompt_craft):
    with pytest.raises(ValueError):
        prompt_craft.create_template("Test Title", "Test Description", "")
