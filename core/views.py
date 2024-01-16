from rest_framework import views
from rest_framework.response import Response


from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemAPIView(views.APIView):
    def get(self, request, pk=None):
        
        if pk:
            items = Item.objects.filter(pk=pk)
        else:
            items = Item.objects.all()

        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ItemSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
