from rest_framework import serializers
from users.models import (Students)
from users.models import (Orders)

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
class GetUsersAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ='__all__'
class GetStudentsAddress(serialisers.ModelsSerilizer):
    class meta:
        model =StudentsAddress
        user_address = GetStudentsAddress

    
