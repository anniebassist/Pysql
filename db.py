from sqlmodel import  create_engine,Session,SQLModel
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv,find_dotenv

#DB_URL="postgresql://postgres:admin@host.docker.internal:5432/postgres"
#DB_URL1="postgresql://postgres:admin@{CONN}:5432/postgres"
print(load_dotenv())

DB_USERNAME=os.getenv("AZURE_POSTGRESQL_USERNAME")
DB_PASSWORD=os.getenv("AZURE_POSTGRESQL_PASSWORD")
DB_URL=os.getenv('AZURE_POSTGRESQL_HOST')
DB_PORT=os.getenv('AZURE_POSTGRESQL_PORT')
DB_NAME=os.getenv('AZURE_POSTGRESQL_DATABASE')




engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/{DB_NAME}')


#creates a metadata of all the classes where table =true
def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
