from src.main.api.models.base_model import BaseModel


class RepayAccountResponse(BaseModel):
    creditId: int
    amountDeposited: float