from typing import Sequence
from AppConstants.constants import REDDIT_USER
from Exceptions import ApplicationException
from utility.database import ENGINE
from sqlalchemy import Row, text
from datetime import datetime


fetch_retieve_query = "SELECT `id`, `name`, `subreddit_name`, `link`, `followers` from {} order by `followers` DESC LIMIT :limit OFFSET :offset;".format(REDDIT_USER)
fetch_retieve_all_query = "SELECT `id`, `name`, `subreddit_name`, `link`, `followers` from {} order by `followers` DESC;".format(REDDIT_USER)
delete_query = "DELETE FROM {} WHERE `id` = :id;".format(REDDIT_USER)


async def insert_update(params: dict) -> None:
    """
    This method is used to insert data in the table
    """
    try: 
        date = datetime.now()
        query = "INSERT INTO {} (`id`, `name`, `subreddit_name`, `reddit_id`, `link`, `followers`, created_date, updated_date) VALUES (:id, :name, :subreddit_name, :reddit_id, :link, :followers, '{}', '{}') ON DUPLICATE KEY UPDATE followers = :followers;".format(REDDIT_USER, date, date)

        with ENGINE.connect() as connection:
            connection.execute(text(query), params)
            connection.commit()
            connection.close()
            
    except Exception as e:
        print(e)
        raise ApplicationException(" SQL Exception Raised: {}".format(e))

async def delete(params: dict) -> None:
    """
    This method is used to insert data in the table
    """
    try: 
        with ENGINE.connect() as connection:
            connection.execute(text(delete_query), params)
            connection.commit()
            connection.close()
            
    except Exception as e:
        print(e)
        raise ApplicationException(" SQL Exception Raised: {}".format(e))


async def fetch_retieve(params: dict) -> Sequence[Row]:
    """
    This method is used to fetch data in the table
    """
    try: 
        with ENGINE.connect() as connection:
            result = connection.execute(text(fetch_retieve_query), params)
            return result.fetchall()
            

    except Exception as e:
        raise ApplicationException(" SQL Exception Raised: {}".format(e))


async def fetch_retieve_all() -> Sequence[Row]:
    """
    This method is used to fetch data in the table
    """
    try: 
        with ENGINE.connect() as connection:
            result = connection.execute(text(fetch_retieve_all_query))
            return result.fetchall()
            

    except Exception as e:
        raise ApplicationException(" SQL Exception Raised: {}".format(e))