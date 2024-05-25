from rest_framework import serializers
from work.models import *


class Userregister_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password','first_name','last_name']
        read_only_fields=['id']


    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class Todo_serializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Task_model
        fields="__all__"
        read_only_fields=["id","created_date","user","completed"]