import pytest
from src.main.api.classes.api_manger import ApiManger


@pytest.fixture
def api_manager(created_obj):
    return ApiManger(created_obj)