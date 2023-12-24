from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
path('new_conversation/', views.new_conversation, name='new_conversation')
]
