import pytest

from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.credit_account_request import CreditAccountRequest
from src.main.api.models.repay_account_request import RepayAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_user_request(api_manager: ApiManger):
        user_request = RandomModelGenerator.generate(CreateUserRequest)
        api_manager.admin_steps.create_user(user_request)
        return user_request

@pytest.fixture
def create_credituser_request(api_manager: ApiManger):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = "ROLE_CREDIT_SECRET" # возможно улучшить реализацию через генератор, но не точно
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_2users_request(api_manager: ApiManger):
    user1_request = RandomModelGenerator.generate(CreateUserRequest)
    user2_request = RandomModelGenerator.generate(CreateUserRequest)
    return user1_request, user2_request

@pytest.fixture
def deposit_account_request(api_manager: ApiManger, create_user_request: CreateUserRequest):
    response = api_manager.user_steps.create_account(create_user_request)
    accountid = response.id
    amount = 1500 # допилить генератор
    user_request = DepositAccountRequest(accountId=accountid, amount=amount)
    return user_request

@pytest.fixture
def transfer_account_request(
        api_manager: ApiManger,
        create_user_request: CreateUserRequest,
        deposit_account_request: DepositAccountRequest
):
    account1 = api_manager.user_steps.deposit_account(create_user_request, deposit_account_request)
    from_id = account1.id
    account2 = api_manager.user_steps.create_account(create_user_request)
    to_id = account2.id
    amount = 1500 # допилить генератор
    # подумать как быть с 2 пользаками, скорее всего внутри с помощью админа + генератора просто запиливать его
    # чтобы обойти огриничение фикстры + через гет получать инфу для ассерта
    # или вообще другая логика
    user_request = TransferAccountRequest(fromAccountId=from_id, toAccountId=to_id, amount=amount)
    return user_request

@pytest.fixture
def credit_account_request(api_manager: ApiManger, create_credituser_request: CreateUserRequest):
    account = api_manager.user_steps.create_account(create_credituser_request)
    account_id = account.id
    amount = 9000 # возможно нужен генератор
    termmonths = 12
    user_request = CreditAccountRequest(accountId=account_id, amount=amount, termMonths=termmonths)
    return user_request

@pytest.fixture
def repay_account_request(
        api_manager: ApiManger,
        create_credituser_request: CreateUserRequest,
        credit_account_request: CreditAccountRequest
):
    credit1 = api_manager.user_steps.credit_account(create_credituser_request, credit_account_request)
    for_credit_id = credit1.creditId
    for_credit_account = credit1.id
    amount = credit1.amount
    user_request = RepayAccountRequest(creditId=for_credit_id, accountId=for_credit_account, amount=amount)
    # Пока идея сделать get метод в реквестер и через него получать необходимую инфу. И ее же использовать для ассерта
    # Либо за счет степов хранить все
    return user_request