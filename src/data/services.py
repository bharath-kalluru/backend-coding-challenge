from sqlalchemy.orm import Session
from src.data.models import City
from src.data.schemas import CityCreate
from sqlalchemy.exc import SQLAlchemyError

def create_city(db: Session, city: CityCreate):
    try:
        db_city = City(name=city.name, latitude=city.latitude, longitude=city.longitude)
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
        return db_city
    except SQLAlchemyError as e:
        print(f"An error occurred during city creation: {str(e)}")
        raise e

def get_city(db: Session, city_id: int):
    try:
        return db.query(City).filter(City.id == city_id).first()
    except SQLAlchemyError as e:
        print(f"An error occurred while retrieving city: {str(e)}")
        raise e
