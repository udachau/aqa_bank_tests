import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager: ApiManger):
        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username, ''
        assert response.user.role == "ROLE_ADMIN", ''

    def test_login_user(self, api_manager: ApiManger, create_user_request: CreateUserRequest):
        response = api_manager.admin_steps.login_user(create_user_request)

        assert create_user_request.username == response.user.username, ''
        assert response.user.role == "ROLE_USER", ''