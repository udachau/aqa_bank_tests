import pytest

from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest


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
        "amount_dep, amount_transf",
        [
            (1000, 499.12),
            (9000, 10000.01)
        ]
    )
    def test_account_invalid_transfer(
            self,
            api_manager: ApiManger,
            create_user_request: CreateUserRequest,
            deposit_account_request: DepositAccountRequest,
            amount_dep: float,
            amount_transf: float
    ):
        deposit_account_request.amount = amount_dep
        account1 = api_manager.user_steps.deposit_account(create_user_request, deposit_account_request)
        from_id = account1.id
        account2 = api_manager.user_steps.create_account(create_user_request)
        to_id = account2.id
        user_request = TransferAccountRequest(fromAccountId=from_id, toAccountId=to_id, amount=amount_transf)
        api_manager.user_steps.invalid_transfer_account(create_user_request, user_request)

