from rest_framework.serializers import ModelSerializer
from token_auth.models import *



class EmployeeSerializer(ModelSerializer):
    class Meta :
        model = Emp
        fields = '__all__'


