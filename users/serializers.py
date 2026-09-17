from rest_framework import serializers
from .models import Resume,Profile
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ProfileSerializer(serializers.ModelSerializer):
    
    user_username = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Profile
        fields = ['id','user','user_username','role','phone']
        read_only_fields = ['user']


class ResumeSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ['user']



class RegisterSerializer(serializers.Serializer):
    password  = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES,write_only = True)
    phone = serializers.CharField(required = False,allow_blank = True)
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ('username','password')

    def create(self,validated_data):
        role = validated_data.pop('role',None)
        phone = validated_data.pop('phone','')
        username = validated_data.pop('username',None)
        password = validated_data.pop('password',None)

        user = User.objects.create_user(
            username=username,
            password=password,
            **validated_data

        )
        Profile.objects.create(
            user = user,
            role = role ,
            phone = phone
        )

        return user
        





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self,data):
        user = authenticate(
            username = data['username'],
            password = data['password'],
        
        )
        if user is None:
            raise serializers.ValidationError(
                'Пароль или имя не представлены '
            )

        data ['user'] = user
        return data 