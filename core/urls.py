
from django.urls import path
from .views import ItemAPIView



urlpatterns = [
    path('', ItemAPIView.as_view() ),
    path('<int:pk>', ItemAPIView.as_view() ),
]