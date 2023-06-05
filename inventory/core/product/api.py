from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Product
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from core.product.serializers import ProductSerializer


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def product_details(request, product_id):
    try:
        user_object = Product.objects.get(id=product_id)
        serializer = ProductSerializer(user_object)
    except Product.DoesNotExist:
        return Response({'status': 'error', 'message': 'product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if user_object:
        return JsonResponse(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
