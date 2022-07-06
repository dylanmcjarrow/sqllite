import logging
from datetime import datetime

from fastapi.param_functions import Depends
from sqlalchemy import desc
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import expression

from minitulip.db.db import get_db
from minitulip.db.models.temp import Temp

log = logging.getLogger(__name__)


class TempCRUD:
    def __init__(self, session: Session = Depends(get_db)) -> None:
        self.session = session

    def create_temp(self, number):

        if type(number) is not int:
            raise Exception(
                f"Number is reqired to be type int [number = {type(number)}]"
            )

        new_temp = Temp(number=number)

        self.session.add(new_temp)
        self.session.commit()
        self.session.refresh(new_temp)
        return new_temp

    def delete_temp_by_id(self, id):

        temp_to_delete = self.read_temp_by_id(id)

        if temp_to_delete:
            self.session.delete(temp_to_delete)
            self.session.commit()

    def read_all_temp(self):

        return self.session.query(Temp).all()

    def read_temp_by_id(self, id):

        return self.session.query(Temp).filter(Temp.id == id).first()
