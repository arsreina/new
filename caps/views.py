from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *


class MainMenuListAPIView(ListAPIView):
    queryset = Cap.objects.all()
    serializer_class = CapMainMenuSerializer
    permission_classes = [IsAuthenticated]


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer
    permission_classes = [IsAuthenticated]


class CapViewSet(ModelViewSet):
    queryset = Cap.objects.all()
    serializer_class = CapListCreateSerializer
    permission_classes = [IsAdminUser]


class BrandUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartValidateAbstractSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class CapUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cap.objects.all()
    serializer_class = CapUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

