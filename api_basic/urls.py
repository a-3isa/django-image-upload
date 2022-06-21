from django.urls import path
from .views import  Images
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'',Images,basename='')

urlpatterns = [
    
    path('', Images.as_view()),
    
]


