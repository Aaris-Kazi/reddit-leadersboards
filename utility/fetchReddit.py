from httpx import AsyncClient, Response

from AppConstants.constants import DEFAULT_OFFSET, END, LIMIT, MAX_REDIRECT, SUCCEED, TIMEOUT, URL
from Exceptions.ApplicationException import ApplicationExcption
from utility.common_operations import delete, fetch_retieve, fetch_retieve_all, insert_update
from utility.json_utils import deleteParams, params, serializingResponse, serializingResponseRank


client = AsyncClient(max_redirects=MAX_REDIRECT, timeout=TIMEOUT)

async def insertUpdateData(username: str) -> None:
    async with AsyncClient(timeout=TIMEOUT) as client:
        url = URL+username+END
        print(url)
        headers = {'Content-Type': 'application/json', 'Cookie': 'csv=2; edgebucket=rI21wmwpsnlzMgghDO; loid=000000000x9hq5xcx9.2.1711802804129.Z0FBQUFBQm1DQW0wam1MUTZON2ViTXpPYllwZ19XSTgzeWtieEhqVlRPbjlNOFY4N0U0TVZGamxHZXphQTdzZWtyY0pRYU90WldrZUQzZXFxdWdQbWdjZzVlcUF3WGJUaDljNGdFYUhRTlVoQXkwcWNFZE5LNkh6OE1JUWgxYXNvYmJhT29UelNhRHg; session_tracker=edgrqlagnbihegljea.0.1711802804138.Z0FBQUFBQm1DQW0wdnROeHVZVldHeUU2REFsTkg5eUNobmVLeTlCaEl0SlpKSUU5OVk5djFNa2U1enhRYS1zNGVkOGdmV3JtWnZyVXNHT1RsTlZXelFDeVVuekhrVGhXR3FWWVJsd05tZDlaWHhJZnowbVBiNTJzdnVhZWZDdWtZZkFsY1RESmhCeFI'}
        response: Response = await client.get(url, headers=headers)
        if response.status_code == SUCCEED:

            query_params = await params(response.json())
            await insert_update(query_params)
            
        else:
            print("for url {}".format(url))
            print("Unable to get the data {}".format(response.status_code))
            # print("Unable to get the data {}".format(response.text))
            raise ApplicationExcption("Unable to get the data {}".format(response.status_code))


async def deleteData(id: str) -> None:
    params = await deleteParams(id)

    await delete(params)
    
    

async def fetchData(offset: int = DEFAULT_OFFSET) -> list[dict]:
    params = {
        "limit": LIMIT,
        "offset": offset
    }

    rows = await fetch_retieve(params)
    result = await serializingResponse(rows)

    return result
    

async def fetchAllData() -> list[dict]:
    rows = await fetch_retieve_all()
    result = await serializingResponseRank(rows)

    return result
