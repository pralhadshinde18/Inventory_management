from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from core.address.models import Address
from core.address.serializers import AddressSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def address_details(request, address_id):
    try:
        address_object = Address.objects.get(id=address_id)
        serializer = AddressSerializer(address_object)
        return JsonResponse(serializer.data)
    except Address.DoesNotExist:
        return Response({'status': 'error', 'message': 'Address does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def address_list(request):
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def create_address(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_address(request, address_id):
    address = Address.objects.get(id=address_id)
    serializer = AddressSerializer(instance=address, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_address(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
    except Address.DoesNotExist:
        return Response({"error": "address not found."}, status=status.HTTP_404_NOT_FOUND)
    address.delete()
    return Response({"message": "address deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
