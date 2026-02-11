
import asyncio
import aiohttp
from typing import List

from request import BatchRequest
from response import BatchResponse
from transport import AsyncHTTPTransport


class BatchClient:
    def __init__(self, max_concurrency: int = 50):
        self.max_concurrency = max_concurrency
        self.transport = AsyncHTTPTransport()

    async def _execute_async(self, requests: List[BatchRequest]) -> List[BatchResponse]:
        semaphore = asyncio.Semaphore(self.max_concurrency)

        connector = aiohttp.TCPConnector(
            limit=self.max_concurrency,
            ssl=True
        )

        async with aiohttp.ClientSession(connector=connector) as session:

            async def bound_send(request: BatchRequest):
                async with semaphore:
                    return await self.transport.send(session, request)

            tasks = [
                asyncio.create_task(bound_send(req))
                for req in requests
            ]

            return await asyncio.gather(*tasks)

    def execute(self, requests: List[BatchRequest]) -> List[BatchResponse]:
        return asyncio.run(self._execute_async(requests))
