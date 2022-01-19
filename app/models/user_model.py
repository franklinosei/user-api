from sqlalchemy import Column, Float, Integer, String

from utilities.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    weight = Column(Float)
    description = Column(String, nullable=True)
