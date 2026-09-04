import pytest


@pytest.mark.api_my
class TestCreditAccount:
    def test_account_credit(self, api_manager, create_credituser_request, credit_account_request):
        response = api_manager.user_steps.credit_account(create_credituser_request, credit_account_request)

        assert response.id == credit_account_request.accountId
        assert response.amount == credit_account_request.amount
        assert  response.termMonths == credit_account_request.termMonths
