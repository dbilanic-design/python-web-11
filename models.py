from sqlalchemy import Column, Integer, String, Date
from database import Base

class Contact(Base):
    tablename = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    birthday = Column(Date)
    extra = Column(String, nullable=True)
