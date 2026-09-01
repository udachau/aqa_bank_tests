from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass

@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint:
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url="/admin/create",
        response_model = CreateUserResponse
    )