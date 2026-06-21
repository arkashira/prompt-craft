import pytest
from prompt_craft import PromptCraft, Template

def test_list_templates():
    craft = PromptCraft("api_token")
    templates = craft.list_templates()
    assert len(templates) == 2
    assert templates[0].id == 1
    assert templates[0].title == "Template 1"
    assert templates[0].version == "1.0"

def test_to_json():
    craft = PromptCraft("api_token")
    craft.templates = [
        Template(1, "Template 1", "1.0"),
        Template(2, "Template 2", "2.0"),
    ]
    json_data = craft.to_json()
    assert json_data == '[{"id": 1, "title": "Template 1", "version": "1.0"}, {"id": 2, "title": "Template 2", "version": "2.0"}]'

def test_main_list():
    import sys
    import io
    import argparse
    from unittest.mock import patch
    from prompt_craft import main
    with patch("sys.argv", ["prompt_craft", "list", "--api-token", "api_token"]):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            main()
    assert fake_stdout.getvalue().strip() == '[{"id": 1, "title": "Template 1", "version": "1.0"}, {"id": 2, "title": "Template 2", "version": "2.0"}]'

def test_main_error():
    import sys
    import io
    import argparse
    from unittest.mock import patch
    from prompt_craft import main
    with patch("sys.argv", ["prompt_craft", "list", "--api-token", "api_token"]):
        with patch("prompt_craft.PromptCraft.list_templates", side_effect=Exception("Test error")):
            with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
                with patch("sys.exit") as exit_mock:
                    main()
    assert fake_stderr.getvalue().strip() == "Error: Test error"
    exit_mock.assert_called_once_with(1)
