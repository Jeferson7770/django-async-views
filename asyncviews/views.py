import asyncio
import httpx
from django.http import HttpResponse


async def http_call_async(request):
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.github.com/")
        print(r)

    return HttpResponse("Exercício concluído com sucesso!")
