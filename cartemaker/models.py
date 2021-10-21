from django.conf import settings
from django.db import models as m
from rpgmaster.models import Group

from django.utils.translation import gettext_lazy as _

# Create your models here.

class HexaMap(m.Model):
    NAME=m.CharField(max_length=50)
    GROUPE=m.ForeignKey(Group, on_delete=m.CASCADE)

class BgHexagone(m.Model):
    GROUP = m.ForeignKey(Group, on_delete=m.CASCADE) 
    BG_COLOR=m.CharField(max_length=7,default="#FFFFFF")
    BD_COLOR=m.CharField(max_length=7,default="#000000")
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR / "cartemaker" / "imgs" / "bg")
    PATH_HEXA=m.FilePathField(path=settings.CARTEMAKER_CACHE_FOLDER / "bg")

class ImgHexagone(m.Model):
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR)
    PATH_HEXA=m.FilePathField(path=settings.CARTEMAKER_CACHE_FOLDER / "obj")

class IcoHexagone(m.Model):
    PATH_FILE=m.FilePathField(path=settings.BASE_DIR)
    PATH_HEXA=m.FilePathField(path=settings.CARTEMAKER_CACHE_FOLDER / "ico")

class Hexagone(m.Model):
    HEXAMAP=m.ForeignKey(HexaMap, on_delete=m.CASCADE)
    X=m.IntegerField()
    Y=m.IntegerField()
    SIZE=m.IntegerField(default=1)
    BG=m.ForeignKey(BgHexagone, on_delete=m.CASCADE)
    OBJ=m.ForeignKey(ImgHexagone, on_delete=m.CASCADE)
    BG_ENABLE=m.BooleanField(default=True)
    OBJ_ENABLE=m.BooleanField(default=True)
    
class SelectIco(m.Model):
    HEXA=m.ForeignKey(Hexagone, on_delete=m.CASCADE)
    ICO=m.ForeignKey(IcoHexagone, on_delete=m.CASCADE)
    POSITION=m.IntegerField()
    ENABLE=m.BooleanField(default=True)    


