
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.views import APIView
from foodapp import serilalizers
from foodapp import permissions
from foodapp import models
from django.http import HttpResponse
import xlwt
import io

class UserCreate(CreateAPIView):
    serializer_class=serilalizers.UserSerializer

class UserProfileManager(RetrieveUpdateAPIView):
    serializer_class=serilalizers.UserSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_object(self):
        return self.request.user
    
class UserTokenGeneration(ObtainAuthToken):
    serializer_class=serilalizers.UserTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class ItemManager(viewsets.ModelViewSet):
    '''api view for creating ,partial updata,delete item only for the superuser '''
    '''data is sent in the format of json'''
    serializer_class=serilalizers.ItemCreationSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,permissions.ItemCreationPermission]
    queryset=models.Item.objects.all()
    def create(self, request, *args, **kwargs):
        # Handle bulk creation of items using a list of data
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)








    




    
