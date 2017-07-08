from rest_framework import serializers
from .models import Order, Coupon, UsedCoupon, Plan, PaymentMethod


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'date', 'price', 'discount', 'payment_method', 'dream', 'user', 'plan')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'description', 'percent_discount', 'fixed_discount', 'all_products_available', 'dreams',
                  'categories', 'packs', 'expiration_date', 'is_available')


class UsedCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedCoupon
        fields = ('id', 'user', 'coupon', 'date')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'duration', 'description', 'price', 'is_available')


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'description', 'api_key', 'user_auth', 'password_auth', 'is_available')
