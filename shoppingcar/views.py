from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order, Coupon, UsedCoupon, Plan, PaymentMethod
from .serializers import OrderSerializer, CouponSerializer, UsedCouponSerializer, PlanSerializer, PaymentMethodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CouponViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dream to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class UsedCouponViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frame to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = UsedCoupon.objects.all()
    serializer_class = UsedCouponSerializer


class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
