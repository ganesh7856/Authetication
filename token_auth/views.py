from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from token_auth.serializer import *
from token_auth.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from token_auth.permission import IsReadOnly,IsGETOrPATCH,OwnPermission

# Create your views here.

class EmployeeOps(ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    #permission_classes = [IsReadOnly,]
    #permission_classes = [IsGETOrPATCH,]
    #permission_classes = [OwnPermission, ]