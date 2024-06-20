from . import views
from django.urls import path


urlpatterns = [
    #Create
    path('', views.participants, name='participants'),
    #Read
    path('participants_read/<int:id>/', views.participants_read, name='participants_read'),
    #Update
    path('participants_update/<int:id>/', views.participants_update, name='participants_update'),
    #Delete
    path('participants_delete/<int:id>', views.participants_delete, name='participants_delete'),
]