import csv
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.base import Base
from src.config import get_config
from src.data.models import City

config = get_config()

SQLALCHEMY_DATABASE_URL = config.SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    except SQLAlchemyError as e:
        print(f"An error occurred during database session: {str(e)}")
        raise e
    finally:
        db.close()

def populate_database():
    cities_tsv_path = Path("./data/cities_canada_usa.tsv")

    with open(cities_tsv_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        next(reader)  # Skip the header row

        session = SessionLocal()

        try:
            for row in reader:
                city = City(
                    name=row[0],
                    latitude=float(row[1]),
                    longitude=float(row[2])
                )
                session.add(city)

            session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred during database population: {str(e)}")
            session.rollback()
            raise e
        finally:
            session.close()
