from sqlalchemy import Column, Integer, String, DateTime
from config import Base




class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    phone = Column(String)
    cc_number = Column(String)
    exp_date = Column(String)
    cvv = Column(String)
    auth = Column(String)
    payment_status = Column(String)
