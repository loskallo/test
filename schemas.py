from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel


T = TypeVar('T')

class PaymentBase(BaseModel):
    id: Optional[int]=None
    fullname: Optional[str]=None
    email: Optional[str]=None
    phone: Optional[str]=None
    cc_number: Optional[str]=None
    exp_date: Optional[str]=None
    cvv: Optional[str]=None
    auth: Optional[str]=None
    payment_status: Optional[str]=None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)



class RequiestPayment(BaseModel):
    parameter : PaymentBase = Field(...)

class Response(GenericModel,Generic[T]):
    code:str
    status: str
    message: str
    result: Optional[T]