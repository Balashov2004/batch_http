
import uuid
from typing import Optional, Dict, Any

class BatchRequest:

    def __init__(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
        timeout: int = 10,
    ):
        self.id = str(uuid.uuid4())
        self.method = method.upper()
        self.url = url
        self.headers = headers or {}
        self.data = data
        self.timeout = timeout