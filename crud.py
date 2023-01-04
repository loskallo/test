from sqlalchemy.orm import Session
from model import Payment
from schemas import  PaymentBase


def get_payment(db:Session,skip:int=0,limit:int=100):
    return db.query(Payment).offset(skip).limit(limit).all()

def get_payment_by_id(db:Session,payment_id:int):
    return db.query(Payment).filter(Payment.id == payment_id).first()


def create_payment(db:Session, payment:PaymentBase):
    _payment = Payment(fullname=payment.fullname,
                       email=payment.email,
                       cc_number=payment.cc_number,
                       exp_date=payment.exp_date,
                       cvv=payment.cvv)
    db.add(_payment)
    db.commit()
    db.refresh(_payment)
    return _payment

def remove_payment(db:Session, payment_id:int):
    _payment = get_payment_by_id(db=db,payment_id=payment_id)
    db.delete(_payment)
    db.commit()

def update_payment_status(db:Session, payment_id:int,payment_status:str):
    _payment = get_payment_by_id(db=db, payment_id= payment_id)
    _payment.payment_status = payment_status
    db.commit()
    db.refresh(_payment)
    return _payment
