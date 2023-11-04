from rest_framework import serializers
from .models import Patient_Records, Department
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '_all_'
        # fields = ("Name","Diagnostics","Specialization")

class DepartmentDoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '_all_'
        # fields = ("Name","Diagnostics","Specialization")

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '_all_'
        fields = ("id", "first_name", "last_name")

class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '_all_'
        fields = ("id", "first_name", "last_name")

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '_all_'
        fields = ("id", "first_name", "last_name")

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '_all_'
        fields = ("id", "first_name", "last_name")

class PatientRecordsSerializer(serializers.ModelSerializer):
    Department_Name = serializers.CharField(source='Department_id.Name', read_only=True)
    Doctor_Name = serializers.CharField(source='Doctor_id.first_name', read_only=True)
    Patient_Name = serializers.CharField(source='Patient_id.first_name', read_only=True)
    class Meta:
        model = Patient_Records
        # fields = '_all_'
        fields = ("Record_id","Created_date", "Department_Name", "Doctor_Name", "Patient_Name")


User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return data
        raise serializers.ValidationError('Invalid username or password')




class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return User