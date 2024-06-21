from . import views
from django.urls import path, include
from rest_framework import routers
from .api import ActivityViewSet

router = routers.DefaultRouter()

router.register('', ActivityViewSet, 'activities')


urlpatterns = [
    #Create
    path('', views.activities, name='activities'),
    #Read
    path('activities_read/<int:id>/', views.activities_read, name='activities_read'),
    #Update
    path('activities_update/<int:id>/', views.activities_update, name='activities_update'),
    #Delete
    path('activities_delete/<int:id>', views.activities_delete, name='activities_delete'),
    #API
    path('api/', include(router.urls)),
]