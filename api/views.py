from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ComapanyviewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

    @action (detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=company.object.get(pk=pk)
            emps=Employee.object.filter(company=company)
            emps_serializer=EmployeeSerializers(emps,many=True,context ={'request':request})
            return Response(emps_serializer.data)
        except Exception as e :
            print(e)
            return Response({
                'message':'Company might not exists !! error'
            })
        

class EmployeeviewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers