from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from announcement.models import Item
from announcement.serializers import ItemSerializer

class ItemListAPIView(ListAPIView):
    queryset = Item.ojects.all()
    serializer_class = ItemSerializer
    
class ItemDetailAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemCreateAPIView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer