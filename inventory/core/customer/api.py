from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .models import Customer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from core.customer.serializers import CustomerSerializer


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def customer_details(request, customer_id):
    try:
        customer_object = Customer.objects.get(id=customer_id)
        serializer = CustomerSerializer(customer_object)
        return JsonResponse(serializer.data)
    except Customer.DoesNotExist:
        return Response({'status': 'error', 'message': 'customer does not exist'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@renderer_classes([JSONRenderer])
def customer_list(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return Response({"error": "customer not found."}, status=status.HTTP_404_NOT_FOUND)
    customer.delete()
    return Response({"message": "customer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

