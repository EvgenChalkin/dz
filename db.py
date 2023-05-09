from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/jojo")
session = create_session(bind=engine)

def add(name, num, index):
    session.execute(text(f"INSERT INTO public.school(name, class_number, class_index) VALUES ('{name}', '{num}', '{index}')"))
    session.commit()
    session.close()
