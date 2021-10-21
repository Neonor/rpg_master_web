from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from cartemaker.forms import BgHexagone,FromNewHexaMap
from cartemaker.cacher import cache_bg

from rpgmaster.models import GroupUser,Group
from cartemaker.models import HexaMap

from os import listdir

from lib.reponses import template

@template('cartemaker/templates/home.html')
def index(request):
    mygroups = ingroups = []
    if request.user.is_authenticated:
        group_user = GroupUser.objects.filter(USER=request.user)
        mygroups = [gu.GROUP for gu in group_user if gu.ADMIN]
        ingroups = [gu.GROUP for gu in group_user if not gu.ADMIN]
    return {"mygroups":mygroups,"ingroups":ingroups}

def new_map(request,group_id):
    if request.method == "POST":
        f_new_map = FromNewHexaMap(request.POST)
        if f_new_map.is_valid():
            new_map = f_new_map.save(commit=False)
            new_map.GROUP = Group.objects.filter(pk=group_id).first()
            new_map.save()
            return HttpResponse("")

    template = loader.get_template('cartemaker/templates/form/new_map.html')
    form_new_group = FromNewHexaMap()
    return HttpResponse(template.render({"new_group":form_new_group}, request))

@template('cartemaker/templates/carte_editor.html',["carte.css"],["carte.js"])
def carte_editor(request):
    form_bg_hexa = BgHexagone()
    if request.method == "POST":
        form_bg_hexa = BgHexagone(request.POST)
        if form_bg_hexa.is_valid():
            path_hexa = cache_bg(form_bg_hexa.cleaned_data["PATH_FILE"],
                     form_bg_hexa.cleaned_data["BG_COLOR"],
                     form_bg_hexa.cleaned_data["BD_COLOR"])
            print(form_bg_hexa.data,path_hexa)
    
    
    
    return {"bg_hexagone":form_bg_hexa}
 

@template('cartemaker/templates/list_imgs.html')
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

