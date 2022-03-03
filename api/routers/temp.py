from fastapi import APIRouter, Depends

from db.crud.temp_crud import TempCRUD

router = APIRouter()


@router.get("/")
def read_all_temp(temp_crud: TempCRUD = Depends()):
    return temp_crud.read_all_temp()
