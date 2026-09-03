import pytest


@pytest.mark.api
class TestDepositAccount:
    def test_account_deposit(self, api_manager, deposit_account_request):
        response = api_manager.user_steps.deposit_account(deposit_account_request)

        assert response.id == deposit_account_request.accountId
        assert response.balance == deposit_account_request.amount
