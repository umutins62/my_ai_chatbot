from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new_conversation/', views.new_conversation, name='new_conversation'),
    path('activate_conversation/<int:conversation_id>/', views.activate_conversation, name='activate_conversation'),
    path('delete_conversation/<int:conversation_id>/', views.delete_conversation, name='delete_conversation'),
    path('update/', views.update_parameters, name='update'),
]
