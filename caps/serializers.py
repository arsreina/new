from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class CapMainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cap
        fields = 'id brand_name get_name price image is_selected'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name caps'.split()


class CategoryValidateAbstractSerializer(CategorySerializer, serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    caps = CapMainMenuSerializer(many=True, required=False)

    def validate_id(self, id):
        try:
            Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise ValidationError('not found')
        return id


class CategoryListCreateSerializer(CategoryValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Category.objects.get(name=name)
        except Category.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class CategoryUpdateDeleteSerializer(CategoryValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Category.objects.exclude(id=self.context.get('id')).get(name=name)
        except Category.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cap
        fields = \
            'id brand_name get_name name price sizes is_selected image is_in_cart description'.split()


class CapValidateAbstractSerializer(CapSerializer, serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100, required=False, write_only=True)
    price = serializers.IntegerField(min_value=100)
    image = serializers.ImageField(required=False)
    is_selected = serializers.BooleanField(default=False)
    is_in_cart = serializers.BooleanField(default=False)

    def validate_price(self, categories):
        if 'sales' in categories:
            previous_price = serializers.IntegerField(min_value=10)
            return previous_price

    def validate_id(self, id):
        try:
            Cap.objects.get(id=id)
        except Cap.DoesNotExist:
            raise ValidationError('not found')
        return id


class CapListCreateSerializer(CapValidateAbstractSerializer):
    def validate_name(self):
        if self.name:
            try:
                Cap.objects.get(name=self.name)
            except Cap.DoesNotExist:
                return self.name
            raise ValidationError('name is already taken')
        return


class CapUpdateDeleteSerializer(CapValidateAbstractSerializer):
    def validate_name(self):
        if self.name:
            try:
                Cap.objects.exclude(id=self.context.get('id')).get(name=self.name)
            except Cap.DoesNotExist:
                return self.name
            raise ValidationError('name is already taken')
        return


class BrandSerializer(serializers.ModelSerializer):
    caps = CapMainMenuSerializer(many=True, required=False)

    class Meta:
        model = Brand
        fields = 'id name caps'.split()


class BrandValidateAbstractSerializer(BrandSerializer, serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    image = serializers.ImageField()

    def validate_id(self, id):
        try:
            Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            raise ValidationError('not found')
        return id


class BrandListCreateSerializer(BrandValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Brand.objects.get(name=name)
        except Brand.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class BrandUpdateDeleteSerializer(BrandValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Brand.objects.exclude(id=self.context.get('id')).get(name=name)
        except Brand.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = 'id caps delivery get_cost'.split()


class CartValidateAbstractSerializer(CartSerializer, serializers.Serializer):
    delivery = serializers.IntegerField(min_value=100)

    def validate_id(self, id):
        try:
            Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            raise ValidationError('not found')
        return id


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

