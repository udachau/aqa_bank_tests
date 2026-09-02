import logging
import pytest
from typing import List, Any
from src.main.api.classes.api_manger import ApiManger
from src.main.api.models.create_user_response import CreateUserResponse


@pytest.fixture
def created_obj():
    objects: List[Any] = []
    yield objects
    clean_users(objects)

def clean_users(objects: List[Any]):
    api_manager = ApiManger(objects)
    for u in objects:
        if isinstance(u, CreateUserResponse):
            api_manager.admin_steps.delete_user(u.id)
        else:
            logging.warning(f"Error in delete user_id: {u.id}")