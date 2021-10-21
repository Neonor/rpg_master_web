from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from . import views

app_name = 'cartemaker'

urlpatterns = [
    path('', views.index, name='index'),
    path('carte_editor', views.carte_editor, name='carte_editor'),
    path('new_map/<int:group_id>', views.new_map, name='new_map'),
    path('list_imgs', views.list_imgs, name='list_imgs'),
]