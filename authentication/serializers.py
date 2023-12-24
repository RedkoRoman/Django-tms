from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from authentication.models import Gender, CustomUser


class UserSerializer(BaseUserSerializer):

    phone_number = serializers.CharField()
    gender = serializers.ChoiceField(choices=[(gender.name, gender.value) for gender in Gender])
    birth_date = serializers.DateField()

    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'gender', 'birth_date')
        ref_name = 'CustomUserSerializer'


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('email', 'username', 'password', )
        ref_name = 'CustomUserCreateSerializer'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'gender', 'birth_date')
        ref_name = 'CustomUserUpdateSerializer'