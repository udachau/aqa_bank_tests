import pytest

from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def deposit_account_request(api_manager, create_user_request):
    response = api_manager.user_steps.create_account(create_user_request)
    accountId = response.id
    amount = 1500
    user_request = DepositAccountRequest(accountId=accountId, amount=amount)
    return user_request
