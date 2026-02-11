
import requests
from typing import List
from request import BatchRequest
from response import BatchResponse


class SequentialClient:
    def execute(self, batch_requests: List[BatchRequest]) -> List[BatchResponse]:
        responses = []

        for request in batch_requests:
            try:
                response = requests.request(
                    method=request.method,
                    url=request.url,
                    headers=request.headers,
                    data=request.data,
                    timeout=request.timeout,
                )

                responses.append(
                    BatchResponse(
                        request_id=request.id,
                        status=response.status_code,
                        body=response.content,
                    )
                )

            except requests.RequestException as e:
                responses.append(
                    BatchResponse(
                        request_id=request.id,
                        error=str(e),
                    )
                )

        return responses
