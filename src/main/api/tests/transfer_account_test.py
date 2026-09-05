import pytest

from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest


@pytest.mark.api_my
class TestTransferAccount:
    def test_account_transfer(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            transfer_account_request: TransferAccountRequest
    ):
        response = api_manager.user_steps.transfer_account(create_user_request, transfer_account_request)

        assert response.fromAccountId == transfer_account_request.fromAccountId, 'Неправильный id счета отправителя'
        assert response.toAccountId == transfer_account_request.toAccountId, 'Неправильный id счета получателя'

    @pytest.mark.parametrize(
        "invalid_transfer_account_request",
        [
            (1000, 499.12),
            (9000, 10000.01)
        ],
        indirect = True
    )
    def test_account_invalid_transfer(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            invalid_transfer_account_request: TransferAccountRequest
    ):
        response = api_manager.user_steps.invalid_transfer_account(create_user_request, invalid_transfer_account_request)

        assert response.text == '{"error":"Amount must be between 500 and 10000"}', "Сработала другая ошибка"

