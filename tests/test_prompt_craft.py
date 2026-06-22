from prompt_craft import PromptCraft

def test_create_project():
    craft = PromptCraft()
    project = craft.create_project("user@example.com", "My Project")
    assert project.name == "My Project"
    assert len(craft.users["user@example.com"].projects) == 1

def test_edit_prompt():
    craft = PromptCraft()
    craft.create_project("user@example.com", "My Project")
    project = craft.edit_prompt("user@example.com", "My Project", "My Prompt")
    assert len(project.prompts) == 1
    assert project.prompts[0] == "My Prompt"

def test_run_evaluation():
    craft = PromptCraft()
    craft.create_project("user@example.com", "My Project")
    result = craft.run_evaluation("user@example.com", "My Project")
    assert result["result"] == "success"

def test_send_welcome_email():
    craft = PromptCraft()
    result = craft.send_welcome_email("user@example.com")
    assert result["message"] == "Welcome email sent"

def test_get_free_tier_limits():
    craft = PromptCraft()
    limits = craft.get_free_tier_limits()
    assert limits["projects"] == 5
    assert limits["eval_calls"] == 10000

def test_free_tier_project_limit():
    craft = PromptCraft()
    for i in range(5):
        craft.create_project("user@example.com", f"Project {i}")
    try:
        craft.create_project("user@example.com", "Project 6")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Free tier project limit reached"

def test_user_not_found():
    craft = PromptCraft()
    try:
        craft.edit_prompt("unknown@example.com", "My Project", "My Prompt")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "User not found"

def test_project_not_found():
    craft = PromptCraft()
    craft.create_project("user@example.com", "My Project")
    try:
        craft.edit_prompt("user@example.com", "Unknown Project", "My Prompt")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Project not found"
