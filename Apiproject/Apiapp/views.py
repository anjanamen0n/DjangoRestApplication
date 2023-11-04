# Create your views here.


from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.decorators import action 
from rest_framework import status,generics
from .serializers import DepartmentSerializer, DoctorSerializer, DoctorDetailSerializer, PatientSerializer,PatientDetailSerializer,UserRegistrationSerializer, PatientRecordsSerializer,UserLoginSerializer
from .models import Department, Patient_Records
from django.contrib.auth.models import User

# class DepartmentView(viewsets.ModelViewSet):
    
#     serializer_class = DepartmentSerializer
    
#     queryset = Department.objects.all()

class DepartmentView(APIView):

    def get(self, request, *args, **kwargs):
        result = Department.objects.all()
        serializers = DepartmentSerializer(result, many=True)
        return Response({'status': 'success', "departments":serializers.data}, status=200)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
class DepartmentDoctorsView(APIView):

    def get(self, request, *args, **kwargs):
        result = Department.objects.all()
        serializers = DepartmentSerializer(result, many=True)
        return Response({'status': 'success', "departments":serializers.data}, status=200)

# to get all doctors list, ids and names
class DoctorView(APIView):

    def get(self, request, *args, **kwargs):
        result = User.objects.filter(groups__name='Doctors')
        serializers = DoctorSerializer(result, many=True)
        return Response({'status': 'success', "doctors":serializers.data}, status=200)
    
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

# to get particular doctor details
class DoctorDetailView(APIView):

    def get(self, request, id=None):
        try:
            result = User.objects.get(id=id, groups__name="Doctors")
            serializers = DoctorDetailSerializer(result)
            return Response({'status': 'success', "doctor_details":serializers.data}, status=200)
        except User.DoesNotExist:
            return Response({'status': 'fail', "doctor_details":"Doctor does not exist"}, status=200)
    
    # def post(self, request):
    #     serializer = DoctorSerializer(data=request.data)  
    #     if serializer.is_valid():  
    #         serializer.save()  
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
    #     else:  
    #         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  


# to get all patients list, ids and names
class PatientView(APIView):

    def get(self, request, *args, **kwargs):
        result = User.objects.filter(groups__name='Patients')
        print(result.query)
        serializers = PatientSerializer(result, many=True)
        return Response({'status': 'success', "patients":serializers.data}, status=200)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
        

# to get particular patient details
class PatientDetailView(APIView):

    def get(self, request, id=None):
        print(User.objects.get(id=id, groups__name="Patients").exists())
        try:
            result = User.objects.get(id=id, groups__name="Patients")
            serializers = PatientDetailSerializer(result)
            return Response({'status': 'success', "patient_details":serializers.data}, status=200)
        except User.DoesNotExist:
            return Response({'status': 'fail', "patient_details":"Patient does not exist"}, status=200)
        

# to get all patient records
class PatientRecordsView(APIView):

    def get(self, request, *args, **kwargs):
        result = Patient_Records.objects.all()
        print(result.query)
        serializers = PatientRecordsSerializer(result, many=True)
        return Response({'status': 'success', "patients":serializers.data}, status=200)
        
    
    def get_extra_actions():
        # Your custom action logic here
        return Response({'message': 'Custom action executed'})
        
    
    
    def post(self, request):
        serializer = PatientRecordsSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
