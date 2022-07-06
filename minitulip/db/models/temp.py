from sqlalchemy import Column, DateTime, Integer, func
from minitulip.db.db import Base

from pydantic import BaseModel


class Newtemp(BaseModel):
    number: int


class Temp(Base):

    __tablename__ = "Temp"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    created = Column(
        DateTime(timezone=False),
        nullable=False,
        server_default=func.now(),
    )
