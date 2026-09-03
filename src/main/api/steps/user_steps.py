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

    def deposit_account(self, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequesters(
            RequestSpecs.auth_headers(username=deposit_account_request.username, password=deposit_account_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response