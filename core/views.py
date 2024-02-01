from rest_framework import views, exceptions, mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters

from .models import Item
from .serializers import ItemSerializer
from user_app.authentication import JWTAuthentication


# Create your views here.
class ItemAPIView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

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

    def delete(self, request, pk: None):
        try:
            item_to_delete = Item.objects.get(pk=pk)
            item_to_delete.delete()
        except:
            raise exceptions.ParseError("Please enter a valid item key")

        return Response({"message": "Item Deleted"}, status=204)


class ItemGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    # queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'category']
    
    def get_queryset(self):
        category = self.request.query_params.get('category')
        
        queryset = Item.objects.all()
        if category:
            queryset = queryset.filter(category=category)
            
        return queryset
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemRetrieveAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
