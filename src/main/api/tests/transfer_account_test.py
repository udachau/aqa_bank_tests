import pytest


@pytest.mark.api_my
class TestTransferAccount:
    def test_account_transfer(self, api_manager, create_user_request, transfer_account_request):
        response = api_manager.user_steps.transfer_account(create_user_request, transfer_account_request)

        assert response.fromAccountId == transfer_account_request.fromAccountId
        assert response.toAccountId == transfer_account_request.toAccountId
        assert response.fromAccountIdBalance == 0