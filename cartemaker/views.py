from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import mimetypes

from os import listdir

from .lib_carte_maker import new_xlsx,make_carte
from lib import reponses

@reponses.template('cartemaker/templates/home.html')
@reponses.menu
@reponses.trad
def index(request):
    return
 

@reponses.template('cartemaker/templates/list_imgs.html')
@reponses.menu
@reponses.trad
def list_imgs(request):
    imgs = {}
    for enter in [enter for enter in listdir("static/imgs/list_map") if ".png" in enter]:
        fol = enter.split("__")[0]
        if not fol in imgs:
            imgs[fol] = []
        imgs[fol].append("imgs/list_map/%s" % enter)
    for enter in imgs:
        imgs[enter].sort()
    return {"imgs":imgs}

def get_new_xlsx(request):
    response = HttpResponse(new_xlsx().read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=carte.xlsx'
    return response

def get_carte(request):
    if request.method == 'POST' and "file" in request.FILES:
        img_byte_arr = make_carte(request.FILES["file"])
        size = len(img_byte_arr.getvalue())

        content_type = mimetypes.guess_type("filename.png")[0]  # Use mimetypes to get file type
        response     = HttpResponse(img_byte_arr,content_type=content_type)  
        response['Content-Length'] = size
        response['Content-Disposition'] = "attachment; filename=carte.png"
        return response
    return HttpResponseRedirect(reverse('cartemaker:index'))