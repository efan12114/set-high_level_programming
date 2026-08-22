from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_db import City, State, Base

def validate_ai_query(username=None, password=None, db_name="orm_practice.db"):
    engine = create_engine(f"sqlite:///{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        results = session.query(City).join(State).all()
        for city in results:
            print(f"{city.id}: {city.name} from {city.state.name}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    validate_ai_query()
