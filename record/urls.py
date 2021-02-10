from django.urls import path

from . import views

urlpatterns = [
    path('', views.record, name='record'),
    path('all', views.all, name='all'),
    path('allwithtime', views.allwithtime, name='allwithtime'),
    path('detail/<str:record_id>', views.detail, name='detail'),
]