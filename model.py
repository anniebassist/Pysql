from sqlmodel import Field,SQLModel,table,Relationship
from datetime import date
from enum import Enum


class genrechoice(Enum):
 ROCk='rock'
 ClASS='classical'   


class Albumbase(SQLModel):
 title:str
 release_date:date
 band_id: int | None =Field(default=None,foreign_key="band.id")



class Bandbase(SQLModel):
 name:str
 genre:genrechoice


class Album(Albumbase,table=True):
 id:int =Field(default=None,primary_key=True)
 band:"Band" =Relationship(back_populates="albums")

class Band(Bandbase,table=True):
 id:int =Field(default=None,primary_key=True)
 albums:list[Album]= Relationship(back_populates="band")
 

class BandCreate(Bandbase):
 albums:list[Albumbase] | None=None

 