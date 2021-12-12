from django.urls import path

from . import views

app_name = 'lab'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id_>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('remove/<int:id_>/', views.remove, name='remove'),
    path('update/<int:id_>/', views.update, name='update'),
]
