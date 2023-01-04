from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


# Replace DATABASE_URI with the connection string for your PostgreSQL database
DATABASE_URI = "postgresql://postgres:zeeaeaa@localhost:5432/paymentdb"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

