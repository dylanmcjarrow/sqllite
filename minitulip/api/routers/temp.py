from fastapi import APIRouter, Depends

from minitulip.db.crud.temp_crud import TempCRUD
from minitulip.db.models.temp import Newtemp

router = APIRouter()


@router.get("/")
def read_all_temp(temp_crud: TempCRUD = Depends()):
    return temp_crud.read_all_temp()


@router.get("/{id:path}")
def read_all_temp(id: int, temp_crud: TempCRUD = Depends()):
    print(id, type(id))
    return temp_crud.read_temp_by_id(id)


@router.post("/")
def create_temp(
    new_temp: Newtemp,
    temp_crud: TempCRUD = Depends(),
):
    return temp_crud.create_temp(new_temp.number)


@router.delete("/{id:path}")
def read_all_temp(id: int, temp_crud: TempCRUD = Depends()):

    return temp_crud.delete_temp_by_id(id)
