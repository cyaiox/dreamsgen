from django.contrib import admin
from .models import Coupon, UsedCoupon, PaymentMethod, Plan, Order


# Register your models here.
admin.site.register(Coupon)
admin.site.register(UsedCoupon)
admin.site.register(PaymentMethod)
admin.site.register(Plan)
admin.site.register(Order)