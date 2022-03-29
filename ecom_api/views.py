#from distutils.log import Log
from django.shortcuts import render


from django.contrib.auth import login


from . import serializers 
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import models
import json 
# Authentication Classes
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication  import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny

# Views Classes
from knox.views import LoginView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView , ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# PAgination and Filter classes
from django_filters.rest_framework import DjangoFilterBackend
# views 

# class CartItemModelViewset(ModelViewSet):
#     queryset = models.CartItem.objects.all()
#     serializer_class = serializers.CartItemSerialzer

#     def get_queryset(self):
#         cart = models.Cart.objects.get(user = self.request.user)
#         cartitems = models.CartItem.objects.filter(cart = cart)

#         return cartitems

class LoginView(LoginView):
    authentication_classes = [BasicAuthentication]

class LoginView(LoginView):
    permission_classes = (AllowAny,)
    
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # print("avdhut",(super(LoginView, self).post(request, format=None)).data)
        # print("user", User.objects.get(username = user.username))#User.objects.get(username = user.username))
        # print(serializers.UserSerializer(user).data)
        data  =super(LoginView, self).post(request, format=None)
        data.data["user"]= serializers.UserSerializer(user).data
        return Response(data.data)
        #return Response(data)


class CartItemAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self ,request , *args , **kwargs):
        data = {}
        cart = models.Cart.objects.get(user = request.user)
        cartitems = models.CartItem.objects.filter(cart = cart)
        i = 1
        for c_item in cartitems :
            data[i]={
                "p_category":c_item.product.category.title,
                "product_id":c_item.product.id,
                "p_name":c_item.product.name , 
                "price":c_item.product.price
            }
            i+=1
        return Response({"Cart Name":"%s" %request.user , "data":data})
    
    def delete(self , request , *args , **kwargs):
        pass


    def post(self , request , *args , **kwargs ):
        id = request.data['pid']
        cart = models.Cart.objects.get(user = request.user)
        product = models.Product.objects.get(id = id )
        c_item = models.CartItem.objects.create(cart=cart,product = product , price = product.price )
        c_item.save()
        
        return Response({"msg":" product added to cart."})




class RegisterAPIView(APIView):
    def post(self , request , *args , **kwargs):
        ser = serializers.RegsterSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"response":'User Created Successfully.'})
    

class CategoryList(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['title']   #filter_backends = [DjangoFilterBackend]


class ProductList(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['name'] 


