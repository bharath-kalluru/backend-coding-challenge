from pydantic import BaseModel

class CityBase(BaseModel):
    name: str
    latitude: float = None
    longitude: float = None

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode = True
