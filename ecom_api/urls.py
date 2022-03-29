from django.urls import path , include

from . import views
from knox.views  import LogoutView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("c-items" , views.CartItemModelViewset , basename='c-items')




app_name = 'ecom'

urlpatterns = [
    path('login/',views.LoginView.as_view() , name = 'login'),
    path('logout/' , LogoutView.as_view() , name = 'logout'),
    path('register/', views.RegisterAPIView.as_view() , name = "register"), 
    path('category/' , views.CategoryList.as_view() , name = "category"),
    path('products/' , views.ProductList.as_view() , name = "products"),
    path('user-cart/',views.CartItemAPIView.as_view() , name='user-cart') ,
    #path('', include(router.urls)),


]