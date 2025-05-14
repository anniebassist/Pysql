from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import init_db,SessionDep,get_session
from model import Album,Band,genrechoice,BandCreate
from sqlmodel import select



#lifespan event . DB created before app taking starts requests

@asynccontextmanager
async def lifespan(app:FastAPI):
 init_db()
 yield

app=FastAPI(lifespan=lifespan)
#app=FastAPI()
#creation of Band 
@app.post("/createBand")
def createBand(bandCreate:BandCreate,session:SessionDep)->Band:
 #instantiate Band with bandcreate details
 band=Band(name=bandCreate.name,genre=bandCreate.genre)
 session.add(band)


 for x in bandCreate.albums:
  alb=Album(title=x.title,release_date=x.release_date,band=band)
  session.add(alb)
 session.commit()
 session.refresh(band)
 return band


#return albums for a particular band
@app.get("/getBandbyID/{id}")
def getBandbyID(id:int,session:SessionDep):
 band=session.get(Band,id)
 statement = select(Album).where(Album.band_id == band.id)
 results = session.exec(statement)
 print (results)
 cv=list[Album]
 cv=results.fetchall()
 return cv