from httpx import AsyncClient

from AppConstants.constants import DEFAULT_OFFSET, END, LIMIT, MAX_REDIRECT, SUCCEED, TIMEOUT, URL
from Exceptions.ApplicationException import ApplicationExcption
from utility.common_operations import delete, fetch_retieve, fetch_retieve_all, insert_update
from utility.json_utils import deleteParams, params, serializingResponse, serializingResponseRank


client = AsyncClient(max_redirects=MAX_REDIRECT, timeout=TIMEOUT)

async def insertUpdateData(username: str) -> None:
    response = await client.get(URL+username+END)
    
    if response.status_code == SUCCEED:
        query_params = await params(response.json())
        await insert_update(query_params)
        
    else:
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
