from rest_framework import viewsets, permissions
from .models import Vacancy, Category
from .serializers import VacancySerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import Is_employer,IsOwner
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter




class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category','city']
    search_fields = ['title','description','company__name']

    ordering_fields = ['salary_from','created_at']
    ordering = ['-created_at']
    def get_permissions(self):
        if self.action == 'create':
            return [Is_employer()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




    

