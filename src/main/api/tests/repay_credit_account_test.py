import pytest


@pytest.mark.api_my
class TestRepayCreditAccount:
    def test_account_repay(self, api_manager, create_credituser_request, repay_account_request):
        response = api_manager.user_steps.repay_account(create_credituser_request, repay_account_request)

        assert response.creditId == repay_account_request.creditId
        assert response.amountDeposited == repay_account_request.amount