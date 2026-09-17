from rest_framework.viewsets import ModelViewSet
from .serializers import ResumeSerializer,ProfileSerializer,RegisterSerializer
from .models import Resume,Profile
from .permissions import Is_job_seeker,isOwner
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

    
    
   
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
    





    

