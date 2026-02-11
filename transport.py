
import aiohttp
import asyncio
from request import BatchRequest
from response import BatchResponse


class AsyncHTTPTransport:
    def __init__(self):
        pass

    async def send(
        self,
        session: aiohttp.ClientSession,
        request: BatchRequest
    ) -> BatchResponse:
        try:
            async with session.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                data=request.data,
                timeout=request.timeout,
            ) as response:
                body = await response.read()
                return BatchResponse(
                    request_id=request.id,
                    status=response.status,
                    body=body,
                )

        except asyncio.TimeoutError:
            return BatchResponse(
                request_id=request.id,
                error="Timeout error",
            )

        except aiohttp.ClientError as e:
            return BatchResponse(
                request_id=request.id,
                error=str(e),
            )
