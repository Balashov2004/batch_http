
from request import BatchRequest
from response import BatchResponse


class AsyncHTTPTransport:

    async def send(self, session, request: BatchRequest) -> BatchResponse:
        try:
            async with session.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                data=request.data,
            ) as response:

                body = await response.read()
                raw_response = (
                    f"HTTP/1.1 {response.status} {response.reason}\r\n"
                    + "".join(f"{k}: {v}\r\n" for k, v in response.headers.items())
                    + "\r\n"
                ).encode() + body

                return BatchResponse(
                    request_id=request.id,
                    status=response.status,
                    body=raw_response,
                )

        except Exception as e:
            return BatchResponse(
                request_id=request.id,
                error=str(e),
            )

