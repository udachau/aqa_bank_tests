import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manger import ApiManger
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.db.crud.user_crud import UserCrudDB as User

@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)],
    )
    def test_create_user_valid(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            db_session: Session
    ):
        response = api_manager.admin_steps.create_user(create_user_request)

        # create_user_response = CreateUserResponse(**response.json()) # как работает?7
        assert create_user_request.username == response.username, 'У пользователя неправильный username или он не создан'
        assert create_user_request.role == response.role, 'У пользователя неправильная роль или он не создан'

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, 'Созданного пользователя нет в БД'

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abv!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0rd"),
            ("Maxx4", "PAS!SW0RD"),
            ("Maxx5", "PasSsw0rd"),
            ("Maxx6", "Pas!swRrd"),
        ]
    )
    def test_create_user_invalid(self, db_session: Session, username: str, password: str, api_manager: ApiManger):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, 'Пользователь создан, ошибка'

    def test_create_2user_valid(
            self,
            api_manager: ApiManger,
            create_2users_request: tuple[CreateUserRequest, CreateUserRequest],
    ):
        user1, user2 = create_2users_request
        response = api_manager.admin_steps.create_user(user1)
        assert user1.username == response.username, 'У пользователя 1 неправильный username или он не создан'
        assert user1.role == response.role, 'У пользователя неправильная роль или он не создан'
        response = api_manager.admin_steps.create_user(user2)
        assert user2.username == response.username, 'У пользователя 2 неправильный username или он не создан'
        assert user2.role == response.role, 'У пользователя неправильная роль или он не создан'


