from django.conf import settings
from django.db import models as m
from rpgmaster.models import Group

# Create your models here.

class BgHexagone(m.Model):
    BG_COLOR=m.CharField(max_length=8,default="000000FF")
    BD_COLOR=m.CharField(max_length=8,default="00000000")
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR)
    PATH_HEXA=m.FilePathField(path=settings.BASE_DIR)

class ImgHexagone(m.Model):
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR)
    PATH_HEXA=m.FilePathField(path=settings.BASE_DIR)

class IcoHexagone(m.Model):
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR)
    PATH_HEXA=m.FilePathField(path=settings.BASE_DIR)

class Hexagone(m.Model):
    BG=BgHexagone()
    IMAGE=ImgHexagone()
    SIZE=m.IntegerField(default=1)
    
class SelectIco(m.Model):
    HEXA=Hexagone()
    ICO=IcoHexagone()
    POSITION=m.IntegerField()
    ENABLE=m.BooleanField(default=True)    

class HexaMap(m.Model):
    NAME=m.CharField(max_length=50)
    GROUPE=Group()
    
class HexaInMap(m.Model):
    HEXAMAP=HexaMap()
    HEXA=Hexagone()
    X=m.IntegerField()
    Y=m.IntegerField()