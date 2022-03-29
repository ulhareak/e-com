


from curses.ascii import US
from . import models 
from django.contrib.auth.models import User
from rest_framework import serializers 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username','first_name' , 'last_name' ,
        'email',
         ]


class RegsterSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.User
        fields = ['username','first_name' , 'last_name' ,
        'password', 'email',
         ]
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        cart = models.Cart.objects.create(user = user)
        cart.save()
        return user

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category 
        fields = '__all__'
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model= models.Product
        fields = '__all__'
class CartItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = '__all__'

class CartItemsSerializerNew(serializers.Serializer):
    pass

