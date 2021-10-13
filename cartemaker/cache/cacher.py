'''
Created on 12 oct. 2021

@author: neonor
'''
import math
import traceback
from os import path,mkdir
from PIL import Image, ImageDraw

from django.conf import settings

CACHE_FOLDER = settings.CARTEMAKER_CACHE_FOLDER #"/home/neonor/eclipse-workspace/rpgmaster/cartemaker/cache"
R = 200
angle_cos = math.cos(math.pi/6)
border_size = 6

def decode_color(value):
    """ décode une chaine str de 8 valeurs hexa (code html sans le # avec l'alpha """
    if not value:
        return (0,0,0,0)
    else:
        return (int(value[0:2],16),int(value[2:4],16),int(value[4:6],16),int(value[6:8],16))

def mask_hexa(x,y,r):
    """ créé un mask hexagonal """
    x,y = x//2,y//2

    p1 = x+r*angle_cos,y+r/2
    p2 = x,y+r
    p3 = x-r*angle_cos,y+r/2
    p4 = x-r*angle_cos,y-r/2
    p5 = x,y-r
    p6 = x+r*angle_cos,y-r/2

    mask = Image.new('RGBA', (x*2,y*2))
    d = ImageDraw.Draw(mask)
    d.polygon((p1,p2,p3,p4,p5,p6), fill='#000')
    return mask


def cache_bg(img_path,bg_color,bd_color=None):
    """
    création d'un hexagone de fond pour la carte, mise en cache
    """
    im = Image.open(img_path)
    x,y = im.size
    r = int(0.45*min([x,y]))
    try:
        
        out = Image.new('RGBA', (2*int(r*angle_cos),r*2),(255,255,255,0))
        mask = mask_hexa(*im.size,r)
        im = im.resize(mask.size)
        out.paste(im, (-(x//2-int(r*angle_cos)),-(y//2-r)), mask)
        im = out.resize((2*int(R*angle_cos),2*R))
        
        size_all = im.size
        size_center = (size_all[0]-border_size,size_all[1]-border_size)
        pos_center = (border_size//2,border_size//2)
        
        
        mask1 = mask_hexa(*size_all,R)
        bg = Image.new('RGBA', size_all,(0,0,0,0))
        bg.paste(Image.new('RGBA', size_all,decode_color(bg_color)),(0,0),mask1)
        im = im.resize(mask1.size)
        bg.alpha_composite(im)

        mask2 = mask_hexa(*size_center,R-border_size)        
        bd = Image.new('RGBA', size_all,(0,0,0,0))
        bd.paste(Image.new('RGBA', size_all,decode_color(bd_color)),(0,0),mask1)
        bd.paste(Image.new('RGBA', size_center,(0,0,0,0)),pos_center,mask2)
        bg.paste(bd, (0,0), bd)
        
        fileout = path.join(CACHE_FOLDER,f"{path.splitext(path.split(img_path)[-1])[0]}.png")
        bg.save(fileout, format='PNG')
        return fileout
    except:
        traceback.print_exc()
        return

def cache_img(img_path,size):
    """
    création d'un hexagone de fond pour la carte, mise en cache
    """
    try:
        im_size = (2*int(R*angle_cos),2*R)
        
        conf_size = {
            3:[int(R/2),int(-R*3/4),1.5],
            4:[0,-int(R),1.6],
            7:[-im_size[0]+im_size[0]//3,-int(im_size[1]/2.5),2.5],
        }
        im = Image.open(img_path)
        x,y = im.size
        _, _, coef = conf_size.get(size,[0,0,1])
        y = int(coef * y * 2*int(R*angle_cos)//x)
        x = int(coef * 2*int(R*angle_cos))
        im = im.resize((x,y))
        
        fileout = path.join(CACHE_FOLDER,f"{path.splitext(path.split(img_path)[-1])[0]}.png")
        im.save(fileout, format='PNG')
        return fileout
    except:
        traceback.print_exc()
        return


if __name__ == "__main__":
    print(cache_bg("/home/neonor/eclipse-workspace/rpgmaster/cartemaker/imgs/bg/scrub.png", "00AA00FF", None))
    print(cache_img("/home/neonor/eclipse-workspace/rpgmaster/cartemaker/imgs/obj/city.png", 1))
    
    
    
    