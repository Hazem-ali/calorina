
from django.urls import path
from .views import ItemAPIView, ItemGenericAPIView, ItemRetrieveAPIView



urlpatterns = [
    # path('', ItemAPIView.as_view() ),
    # path('<int:pk>', ItemAPIView.as_view() ),
    path('', ItemGenericAPIView.as_view() ),
    path('<int:pk>', ItemRetrieveAPIView.as_view() ),
]