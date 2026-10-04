from rest_framework.viewsets import ModelViewSet
from .serializers import ResumeSerializer,ProfileSerializer,RegisterSerializer
from .models import Resume,Profile
from .permissions import Is_job_seeker,isOwner
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
    
   
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [Is_job_seeker]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_permissions(self):
        if self.action == 'create':
            return [Is_job_seeker()]
        elif self.action in ['update','partial_update','destroy']:
            return [isOwner]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    



def home_view(request):
    """View для главной страницы"""
    return render(request, 'users/home.html')

def login_view(request):
    """View для обработки формы входа"""
    error = None
    
    # 1. Если пользователь шлет POST-запрос (нажал кнопку "Войти")
    if request.method == 'POST':
        # Забираем данные из инпутов по их атрибуту 'name'
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        # 2. ПРОВЕРЯЕМ: есть ли такой юзер в базе и верен ли пароль?
        user = authenticate(request, username=user_name, password=user_pass)
        
        if user is not None:
            # 3. ЕСЛИ ВСЁ ОК: создаем сессию (входим на сайт)
            login(request, user)
            # Перенаправляем на главную страницу
            return redirect('home')
        else:
            # ЕСЛИ НЕПРАВИЛЬНО: готовим ошибку для вывода в HTML
            error = "Неверный логин или пароль!"
            
    # Если это обычный GET-запрос (открыли страницу входа) или была ошибка
    return render(request, 'users/login.html', {'error': error})



def register_view(request):
    error = None
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_pass = request.POST.get('password')
        
        # БЭКЕНД-ПРОВЕРКА: занят ли логин?
        if User.objects.filter(username=user_name).exists():
            error = "Пользователь с таким логином уже существует!"
        else:
            # СОЗДАНИЕ ЮЗЕРА: Используем специальный метод create_user!
            # Метод create_user сам автоматически захэширует пароль перед сохранением
            user = User.objects.create_user(username=user_name, email=user_email, password=user_pass)
            
            # Сразу авторизуем его, чтобы после регистрации не нужно было входить заново
            login(request, user)
            return redirect('home')
            
    return render(request, 'users/register.html', {'error': error})


def logout_view(request):
    logout(request)  # Встроенная функция Django очистит сессию
    return redirect('login')  # Перенаправляем на страницу входа

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Вы вышли"}, status=status.HTTP_200_OK)

def home_view(request):
    return render(request, 'users/home.html')

