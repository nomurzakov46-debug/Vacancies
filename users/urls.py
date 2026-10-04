from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet,ProfileViewSet,RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter()


router.register(r'resume',ResumeViewSet)
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    # --- НАШИ КРАСИВЫЕ HTML СТРАНИЦЫ (Для тестов монолита) ---
    path('web/', views.home_view, name='home'),               # Главная будет доступна на /web/
    path('web/login/', views.login_view, name='login'),       # Логин на /web/login/
    path('web/register/', views.register_view, name='register'), # Регистрация на /web/register/
    path('web/logout/', views.logout_view, name='logout'),
     path('', views.home_view, name='home'),
    # --- ТВОЁ ГОТОВОЕ REST API (Не трогаем, пусть работает) ---
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='api_register'), # Переименовали name, чтобы не было конфликта
    path('token/', obtain_auth_token, name='api_token_auth'),
]

