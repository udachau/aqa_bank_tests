import pytest

from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.repay_account_request import RepayAccountRequest


@pytest.mark.api_my
class TestRepayCreditAccount:
    def test_account_repay(
            self,
            api_manager: ApiManger,
            create_credituser_request: CreateUserRequest,
            repay_account_request: RepayAccountRequest
    ):
        response = api_manager.user_steps.repay_account(create_credituser_request, repay_account_request)

        assert response.creditId == repay_account_request.creditId, 'Неправильный id счета для погашения кредита'
        assert response.amountDeposited == repay_account_request.amount, 'Неправильная/неполная сумма погашения кредита'

    def test_account_invalid_repay(
            self,
            api_manager: ApiManger,
            create_credituser_request: CreateUserRequest,
            credit_account_request: CreditAccountRequest
    ):
        credit1 = api_manager.user_steps.credit_account(create_credituser_request, credit_account_request)
        credit_id = credit1.creditId
        credit_account = credit1.id
        amount = credit1.amount - 100
        user_request = RepayAccountRequest(creditId=credit_id, accountId=credit_account, amount=amount)
        api_manager.user_steps.invalid_repay_account(create_credituser_request, user_request)
