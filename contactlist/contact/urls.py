from django.urls import path
from . import views
import profile



urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact', views.addcontact, name='add-contact'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('deletecontact/<str:pk>',views.deletecontact,name='deletecontact'),
    
]
