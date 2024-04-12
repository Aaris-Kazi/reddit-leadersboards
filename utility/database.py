from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from AppConstants.constants import SQLALCHEMY_DATABASE_URL

ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = Session(ENGINE, future=True, autocommit=False, autoflush=False)
BASE = declarative_base()
