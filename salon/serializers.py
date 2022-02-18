from rest_framework import serializers
from .models import Service, Visit, User
from django.core.mail import send_mail
import secrets


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'approximate_time', 'price', 'notes']


class UserSerializer(serializers.ModelSerializer):
    visits = serializers.PrimaryKeyRelatedField(queryset=Visit.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'visits', 'email', 'password', 'first_name', 'last_name', 'role']


class UserSerializerUpdate(serializers.ModelSerializer):
    visits = serializers.PrimaryKeyRelatedField(queryset=Visit.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'visits', 'email', 'first_name', 'last_name', 'role']


class UserSerializerCreate(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise serializers.ValidationError('Username already taken')

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise serializers.ValidationError('Username already taken')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user_token = secrets.token_hex(16)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            token=user_token)
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        send_mail('Verify you account!', f'Yours token: {user_token}', 'szymoncwynar@szymoncwynar.usermd.net',
                  [validated_data['email']])
        return user


class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']


class VisitSerializerUpdate(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    hairdresser = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='HR'))
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='CL'))

    class Meta:
        model = Visit
        fields = ['date', 'service', 'hairdresser', 'client']


class VisitSerializerList(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    hairdresser = UserSerializerView(read_only=True)
    client = UserSerializerView(read_only=True)

    class Meta:
        model = Visit
        fields = ['date', 'service', 'hairdresser', 'client']


class VisitSerializerCreate(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    hairdresser = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='HR'))
    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Visit
        fields = ['date', 'service', 'hairdresser', 'client']


class MyVisitSerializer(serializers.ModelSerializer):
    service = serializers.ReadOnlyField(source='service.name')
    hairdresser = serializers.ReadOnlyField(source='hairdresser.first_name')
    client = serializers.ReadOnlyField(source='client.first_name')

    class Meta:
        model = Visit
        fields = ['id', 'date', 'service', 'hairdresser', 'client']


class MyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']


class UserSerializerMin(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class Verify(serializers.Serializer):
    mail = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    def create(self, validated_data):
        try:
            User.objects.get(email=validated_data['mail'])
        except User.DoesNotExist:
            raise serializers.ValidationError('email does not exist')
        user = User.objects.get(email=validated_data['mail'])
        if user.token == validated_data['token']:
            user.is_active = True
            user.save()
            return user
        else:
            raise serializers.ValidationError('token is invalid!')
