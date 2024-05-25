from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from rest_framework import authentication,permissions
from rest_framework.viewsets import ViewSet,ModelViewSet


# Create your views here.


class Userregister_apiview(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Userregister_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class Todoviewset_view(ViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Task_model.objects.all()
        serializer=Todo_serializer(qs,many=True)
        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=Todo_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task_model.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response({"success":"todo task deleted successfully"})
        else:
            raise serializers.ValidationError('not allowed')
        

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task_model.objects.get(id=id)
        serializer=Todo_serializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            qs=Task_model.objects.get(id=id)
            serializer=Todo_serializer(qs)
            return Response(serializer.data)
        except:
            return Response({"error":"id doesnt exsist"})
        

class Todomodelviewset_view(ModelViewSet):
    queryset=Task_model.objects.all()
    serializer_class=Todo_serializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
        
    # def get_queryset(self):
    #     return Task_model.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)
    

# anagram