from typing import Optional
from pydantic import BaseModel


class UserPostModel(BaseModel):
    rank: int
    name: str
    members:int = 0
    link:str
    icon: str

class ListUserModels(BaseModel):
    data: list = [UserPostModel]

class UserSubredditRequest(BaseModel):
    username: Optional[str] = None
    subreddit: Optional[str] = None