
from sqlalchemy import Column, DateTime, Integer, String, func
from AppConstants.constants import REDDIT_USER
from utility.database import BASE


class UserBases(BASE):
    __tablename__ = REDDIT_USER
    id = Column(String(length=256), primary_key=True, index=True)
    name = Column(String(length=256))
    subreddit_name = Column(String(length=256))
    reddit_id = Column(String(length=256))
    link = Column(String(length=256))
    followers= Column(Integer, default=0)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now())

