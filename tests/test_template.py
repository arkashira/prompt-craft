from template import TemplateService, API
import pytest

def test_create_template():
    service = TemplateService()
    template = {"name": "example", "content": "example content"}
    created_template = service.create_template(1, template)
    assert created_template.id == 1
    assert created_template.name == template["name"]
    assert created_template.content == template["content"]

def test_rate_limit():
    service = TemplateService()
    template = {"name": "example", "content": "example content"}
    for _ in range(5):
        service.create_template(1, template)
    with pytest.raises(Exception):
        service.create_template(1, template)

def test_authenticate():
    api = API()
    with pytest.raises(Exception):
        api.template_service.authenticate("invalid_token")
    assert api.template_service.authenticate("secret_token") == 1

def test_handle_post():
    api = API()
    template = {"name": "example", "content": "example content"}
    response = api.handle_post("secret_token", template)
    assert response["id"] == 1
    assert response["name"] == template["name"]
    assert response["content"] == template["content"]
