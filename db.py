from sqlmodel import  create_engine,Session,SQLModel
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv,find_dotenv

#DB_URL="postgresql://postgres:admin@host.docker.internal:5432/postgres"
#DB_URL1="postgresql://postgres:admin@{CONN}:5432/postgres"
print(load_dotenv())

DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_URL=os.getenv('DB_URL')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')




engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/{DB_NAME}')


#creates a metadata of all the classes where table =true
def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
