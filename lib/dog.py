from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Dog  # Import your Dog model here

def create_table(base, db_url):
    engine = create_engine(db_url)
    base.metadata.create_all(engine)

def save(session, dog):
    try:
        session.add(dog)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error saving dog: {str(e)}")
        return False

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog_id, new_breed):
    try:
        dog = find_by_id(session, dog_id)
        if dog:
            dog.breed = new_breed
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        session.rollback()
        print(f"Error updating breed: {str(e)}")
        return False
