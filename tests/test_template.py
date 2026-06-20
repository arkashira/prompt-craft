from template import API, TemplateService, AuthService, RateLimiter
import pytest

def test_create_template():
    api = API()
    token = api.auth_service.generate_token("user")
    response = api.create_template(token, "test", "content")
    assert response["name"] == "test"
    assert response["content"] == "content"

def test_create_template_invalid_token():
    api = API()
    with pytest.raises(ValueError):
        api.create_template("invalid-token", "test", "content")

def test_create_template_rate_limit_exceeded():
    api = API()
    token = api.auth_service.generate_token("user")
    for _ in range(10):
        api.create_template(token, "test", "content")
    with pytest.raises(ValueError):
        api.create_template(token, "test", "content")

def test_get_template():
    api = API()
    token = api.auth_service.generate_token("user")
    template = api.template_service.create_template("test", "content")
    response = api.get_template(token, template.id)
    assert response["name"] == "test"
    assert response["content"] == "content"

def test_get_template_invalid_token():
    api = API()
    with pytest.raises(ValueError):
        api.get_template("invalid-token", 1)

def test_get_template_template_not_found():
    api = API()
    token = api.auth_service.generate_token("user")
    with pytest.raises(ValueError):
        api.get_template(token, 1)
