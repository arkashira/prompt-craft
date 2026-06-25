from prompt_craft import Prompt, PromptEditor, syntax_highlighting

def test_create_draft():
    editor = PromptEditor()
    prompt = Prompt("Hello {name}", ["name"])
    created_prompt = editor.create_draft(prompt)
    assert created_prompt.text == "Hello {name}"
    assert created_prompt.placeholders == ["name"]

def test_autosave_draft():
    editor = PromptEditor()
    prompt = Prompt("Hello {name}", ["name"])
    autosaved_prompt = editor.autosave_draft(prompt)
    assert autosaved_prompt.text == "Hello {name}"
    assert autosaved_prompt.placeholders == ["name"]

def test_lint():
    editor = PromptEditor()
    prompt = Prompt("Hello {name}", ["name"])
    errors = editor.lint(prompt)
    assert not errors

    prompt = Prompt("Hello", [])
    errors = editor.lint(prompt)
    assert "Missing placeholders" in errors

    prompt = Prompt("Hello {name} {name}", ["name", "name"])
    errors = editor.lint(prompt)
    assert "Duplicate keys" in errors

def test_syntax_highlighting():
    prompt = Prompt("Hello {name}", ["name"])
    highlighted_text = syntax_highlighting(prompt)
    assert highlighted_text == "Hello <span style='color: blue'>{</span>name<span style='color: blue'>}</span>"

def test_sync_to_repo():
    editor = PromptEditor()
    prompt = Prompt("Hello {name}", ["name"])
    synced_prompt = editor.sync_to_repo(prompt)
    assert synced_prompt.text == "Hello {name}"
    assert synced_prompt.placeholders == ["name"]
