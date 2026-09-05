import pytest

from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api_my
class TestDepositAccount:
    def test_account_deposit(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            deposit_account_request: DepositAccountRequest
    ):
        response = api_manager.user_steps.deposit_account(create_user_request, deposit_account_request)

        assert response.id == deposit_account_request.accountId, 'Неправильная id счета пополнения'
        assert response.balance == deposit_account_request.amount, 'Неправильная сумма пополнения'

    @pytest.mark.parametrize("amount", [499.12, 10000.01])
    def test_account_invalid_deposit(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            deposit_account_request: DepositAccountRequest,
            amount: float
    ):
        deposit_account_request.amount = amount
        api_manager.user_steps.invalid_deposit_account(create_user_request, deposit_account_request)

