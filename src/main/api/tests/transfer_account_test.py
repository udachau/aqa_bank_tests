import pytest
from main.api.models.transfer_account_request import TransferAccountRequest
from main.api.requests.deposit_account_requester import DepositAccountRequester
from main.api.requests.transfer_account_requester import TransferAccountRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.models.deposit_account_request import DepositAccountRequest

@pytest.mark.api
class TestAccountTransfer:
    def test_account_transfer(self):
        create_user1_request = CreateUserRequest(username="MaxFrom1", password="Pas!sw0rd", role="ROLE_USER")
        create_user2_request = CreateUserRequest(username="MaxTo1", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user1_request)

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user2_request)

        resp_creation_balance = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxFrom1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        balance_id_from = resp_creation_balance.id

        deposit_account_request_from = DepositAccountRequest(accountId=balance_id_from, amount=2001)

        DepositAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxFrom1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_account_request_from)

        resp_creation_balance = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxTo1", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        balance_id_to = resp_creation_balance.id

        transfer_account_request = TransferAccountRequest(fromAccountId=balance_id_from, toAccountId=balance_id_to, amount=1000)

        response = TransferAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxFrom1", password="Pas!sw0rd"),
            response_spec = ResponseSpecs.request_ok()
        ).post(transfer_account_request)

        assert response.fromAccountIdBalance == 2001 - 1000

        # Параметризовать создание пользователей и счетов + id счета + нормальные проверка