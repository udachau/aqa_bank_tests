from src.main.api.models.base_model import BaseModel


class RepayAccountRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float