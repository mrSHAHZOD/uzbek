from django.shortcuts import get_object_or_404
from rest_framework.views import APIView ,Response
from .serializers import ProductSerializer
from .models import ProductsModel

# Create your views here.

class AllBookVIew(APIView):
    def get(self,request,*args,**kwargs):
        all_product = ProductsModel.objects.all()
        serializer = ProductSerializer(all_product,many=True)
        return Response(serializer.data)

class FirstTypeAllProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = ProductsModel.objects.filter(types = '1')
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)


class SecondTypeAllProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = ProductsModel.objects.filter(types = '2')
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)
    
class ThirdTypeAllProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = ProductsModel.objects.filter(types = '3')
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)
    
class FourthTypeAllProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = ProductsModel.objects.filter(types = '4')
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data)
    
class DetailFirstTypeProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = get_object_or_404(ProductsModel.objects.filter(types = '1'), pk=kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class DetailSecondTypeProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = get_object_or_404(ProductsModel.objects.filter(types = '2'), pk=kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class DetailThirdTypeProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = get_object_or_404(ProductsModel.objects.filter(types = '3'), pk=kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class DetailFourthTypeProductView(APIView):
    def get(self,request,*args,**kwargs):
        product = get_object_or_404(ProductsModel.objects.filter(types = '4'), pk=kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)






