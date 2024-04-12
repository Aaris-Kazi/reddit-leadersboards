from sqlite3 import Row
from typing import Sequence
from AppConstants.constants import _ID, CHILDREN, DATA, FIRST_INDEX, ID, NAME_PREFIX, SUBREDDIT, SUBSCRIBERS, URL


async def datafilter(raw_data: dict) -> dict:
    """
    This method out filter into required data
    :param raw_data: is a dictionary get by the json response of reddit
    :Returns : Required data share for easy to parse
    """
    filter_data = raw_data[DATA][CHILDREN][FIRST_INDEX][DATA]
    return filter_data


async def params(response: dict) -> dict:
    """
    This method out filter into required data
    :param raw_data: is a dictionary get by the json response of reddit
    :Returns : Required data for inserting the data
    """

    data = await datafilter(response)

    query_parameter = {
        "id": data[ID],
        "name": data[SUBREDDIT],
        "subreddit_name": data[SUBREDDIT+NAME_PREFIX],
        "reddit_id": data[SUBREDDIT+_ID],
        "link": data[SUBREDDIT],
        "followers": data[SUBREDDIT+SUBSCRIBERS]
    }
    return query_parameter


async def deleteParams(id: str) -> dict:
    """
    This method out filter into required data
    :param id: is a string get by the request body of reddit
    :Returns : Required data for inserting the data
    """


    query_parameter = {
        "id": id
    }
    return query_parameter


async def serializingResponse(rows: Sequence[Row]) -> list[dict]:
    """
    This method out filter into required data
    :param rows: This comes with the SQL fetch data class
    :Returns : Required list of data
    """
    result = []
    for data in rows:
        result.append({
            "id": data[0],
            "name": data[1],
            "subreddit_name": data[2],
            "link": URL+data[3],
            "followers": data[4]
        })
    return result


async def serializingResponseRank(rows: Sequence[Row]) -> list[dict]:
    """
    This method out filter into required data
    :param rows: This comes with the SQL fetch data class
    :Returns : Required list of data
    """
    result = []
    i =0
    for data in rows:
        i=i+1
        result.append({
            "rank": i,
            "name": data[1],
            "followers": data[4]
        })
    return result