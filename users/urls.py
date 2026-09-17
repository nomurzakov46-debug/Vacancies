from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet,ProfileViewSet,RegisterView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()


router.register(r'resume',ResumeViewSet)
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path ('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
    
    path('token/',obtain_auth_token,name='api_token_auth'),
]
