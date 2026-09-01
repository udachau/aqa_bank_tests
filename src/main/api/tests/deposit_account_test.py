import pytest
from main.api.requests.deposit_account_requester import DepositAccountRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.models.deposit_account_request import DepositAccountRequest

@pytest.mark.api
class TestAccountDeposit:
    def test_account_deposit(self):
        create_user_request = CreateUserRequest(username="MaxTT", password="Pas!sw0rd", role="ROLE_USER")

        CreateUserRequester(
            request_spec=RequestSpecs.auth_headers(username="admin", password="123456"),
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        resp_creation_balance = CreateAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxTT", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_created()
        ).post()

        balance_id = resp_creation_balance.id

        deposit_account_request = DepositAccountRequest(accountId=balance_id, amount=1240.1)

        response = DepositAccountRequester(
            request_spec=RequestSpecs.auth_headers(username="MaxTT", password="Pas!sw0rd"),
            response_spec=ResponseSpecs.request_ok()
        ).post(deposit_account_request)

        assert response.balance == 1240.1
# Доработать логику с вытскиванием ID из созданного счета по анлогией с токеном
# Возможно сделать лучше позитивный тест
# После этого написать негатив, например на сумму 1000 - 9000

