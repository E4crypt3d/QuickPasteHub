from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('paste/create', views.create_paste, name='create_paste'),
    path('pastes', views.ExplorePastes.as_view(), name='explore'),
    path('paste/<str:token>', views.view_paste, name='view_paste'),
    path('paste/<str:token>/edit', views.edit_paste, name='edit_paste'),
]
