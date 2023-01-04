from fastapi import APIRouter, HTTPException,Path,Depends
from config import  SessionLocal
from sqlalchemy.orm import  Session
from schemas import PaymentBase,RequiestPayment,Response,Request

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#post a cc
@router.post('/create')
async def create(request:RequiestPayment,db:Session=Depends(get_db())):
    crud.create_payment(db,payment=request.parameter)
    return Response(code=200,status="OK",message="Payment Created Successfully!").dict(exclude_none=True)

#get all ccs
@router.get('/')
async def get(db:Session=Depends(get_db())):
    _payment = crud.get_payment(db,0,100)
    return Response(code=200,status="OK",message="Fetch all data Successfully!", result=_payment).dict(exclude_none=True)


#get cc by id
@router.get('/{id}')
async def get_by_id(id:int,db:Session=Depends(get_db())):
    _payment = crud.get_payment_by_id(db,id)
    return Response(code=200,status="OK",message="Fetch 1 cc Successfully!", result=_payment).dict(exclude_none=True)



#update_payment_status
@router.get('/update_status')
async def update_payment_status(request:RequiestPayment, db:Session=Depends(get_db())):
    _payment = crud.update_payment_status(db,payment_id=request.parameter.id,payment_status=request.parameter.payment_status)
    return Response(code=200,status="OK",message="status updated Successfully!", result=_payment).dict(exclude_none=True)

#update_payment_status....


@router.delete("/{id}")
async def delete(id:int,db:Session = Depends(get_db())):
    crud.remove_payment(db,payment_id=id)
    return Response(code=200,status="OK",message="CC deleted Successfully!").dict(exclude_none=True)