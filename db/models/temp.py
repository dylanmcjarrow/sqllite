from sqlalchemy import Column, Integer
from db.db import Base

from pydantic import BaseModel


class Newtemp(BaseModel):
    number: int


class Temp(Base):

    __tablename__ = "Temp"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
