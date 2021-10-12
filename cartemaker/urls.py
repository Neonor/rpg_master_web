from django.urls import path

from . import views

app_name = 'cartemaker'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_new_xlsx', views.get_new_xlsx, name='get_new_xlsx'),
    path('get_carte', views.get_carte, name='get_carte'),
    path('list_imgs', views.list_imgs, name='list_imgs'),
]