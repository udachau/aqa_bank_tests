from main.api.models.transfer_account_response import TransferAccountResponse
from main.api.requests.requester import Requester
from src.main.api.models.transfer_account_request import TransferAccountRequest
from requests import Response
import requests

class TransferAccountRequester(Requester):
    def post(self, transfer_account_request: TransferAccountRequest) -> TransferAccountResponse | Response:
        url = f"{self.base_url}/account/transfer"

        response = requests.post(
            url=url,
            json=transfer_account_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return TransferAccountResponse(**response.json())
