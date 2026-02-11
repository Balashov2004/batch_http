
from typing import Optional

class BatchResponse:
    def __init__(
        self,
        request_id: str,
        status: Optional[int] = None,
        body: Optional[bytes] = None,
        error: Optional[str] = None,
    ):
        self.request_id = request_id
        self.status = status
        self.body = body
        self.error = error

    @property
    def ok(self) -> bool:
        return self.error is None and self.status is not None and self.status < 400