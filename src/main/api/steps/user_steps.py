from src.main.api.foundation.requesters.crud_requesters import CrudRequester
from src.main.api.models.repay_account_request import RepayAccountRequest
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.foundation.requesters.validate_requesters import ValidateCrudRequesters
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.foundation.endpoint import Endpoint

class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_max_account(self, create_user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.conflict()
        ).post()
        return response

    def deposit_account(
            self,
            create_user_request: CreateUserRequest,
            deposit_account_request: DepositAccountRequest
    ):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response

    def invalid_deposit_account(
            self,
            create_user_request: CreateUserRequest,
            deposit_account_request: DepositAccountRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_account_request)
        return response

    def transfer_account(
            self,
            create_user_request: CreateUserRequest,
            transfer_account_request: TransferAccountRequest
    ):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_account_request)
        return response

    def invalid_transfer_account(
            self,
            create_user_request: CreateUserRequest,
            user_request: TransferAccountRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(user_request)
        return response

    def credit_account(
            self,
            create_credituser_request: CreateUserRequest,
            credit_account_request: CreditAccountRequest
    ):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=create_credituser_request.username,
                                      password=create_credituser_request.password),
            Endpoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(credit_account_request)
        return response

    def invalid_credit_account(
            self,
            create_credituser_request: CreateUserRequest,
            credit_account_request: CreditAccountRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_credituser_request.username,
                                      password=create_credituser_request.password),
            Endpoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(credit_account_request)
        return response

    def repay_account(
            self,
            create_credituser_request: CreateUserRequest,
            repay_account_request: RepayAccountRequest
    ):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=create_credituser_request.username,
                                      password=create_credituser_request.password),
            Endpoint.REPAY_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(repay_account_request)
        return response

    def invalid_repay_account(
            self,
            create_credituser_request: CreateUserRequest,
            user_request: RepayAccountRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_credituser_request.username,
                                      password=create_credituser_request.password),
            Endpoint.REPAY_ACCOUNT,
            ResponseSpecs.bad_content()
        ).post(user_request)
        return response