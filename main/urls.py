from django.urls import path, include
from . import views as v


urlpatterns = [
    path('', v.index, name='home'),
    path('form/', v.empEntry, name='form'),
    path('record/', v.empRecord, name='record'),
    path('store/', v.empStore, name='store'),
]
