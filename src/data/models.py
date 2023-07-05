from sqlalchemy import Column, Integer, String, Float
from src.base import Base  # Update the import statement

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

