from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Item
@api_view(['GET'])
def getData(request):
    #person = {'name': 'vera'}
    items = Item.objects.all()
    #serialize data
    serialiser = ItemSerializer(items,many=True)

    return Response(serialiser.data)
@api_view(['POST'])
def addItem(request):
    serialiser = ItemSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

