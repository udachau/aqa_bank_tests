import pytest
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.classes.api_manger import ApiManger


@pytest.mark.api_my
class TestCreditAccount:
    def test_account_credit(
            self,
            api_manager: ApiManger,
            create_credituser_request: CreateUserRequest,
            credit_account_request: CreditAccountRequest
    ):
        response = api_manager.user_steps.credit_account(create_credituser_request, credit_account_request)

        assert response.id == credit_account_request.accountId, 'Неправильный id счета получения кредита'
        assert response.amount == credit_account_request.amount, 'Неправильная сумма кредита'
        assert  response.termMonths == credit_account_request.termMonths, 'Неправильный срок кредита'

    @pytest.mark.parametrize(
        "amount",
        [4000, 16000]
    )
    def test_account_invalid_credit(
            self,
            api_manager: ApiManger,
            create_credituser_request: CreateUserRequest,
            credit_account_request: CreditAccountRequest,
            amount: float
    ):
        credit_account_request.amount = amount
        api_manager.user_steps.invalid_credit_account(create_credituser_request, credit_account_request)
