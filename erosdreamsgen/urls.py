"""erosdreamsgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from audio.views import GroupViewSet as GroupAudioViewSet, AudioViewSet
from dream.views import GroupViewSet as GroupDreamViewSet, DreamViewSet, FrameViewSet, PackViewSet
from shoppingcar.views import OrderViewSet, CouponViewSet, UsedCouponViewSet, PlanViewSet, PaymentMethodViewSet
from user.views import ProfileViewSet, AddressViewSet, LogViewSet, WishListViewSet, \
                       ExperienceViewSet, LoginView, LogoutView, UserViewSet, GroupViewSet as GroupUserViewSet

router = routers.DefaultRouter()
router.register(r'groupsaudios', GroupAudioViewSet)
router.register(r'audios', AudioViewSet)
router.register(r'groupsdreams', GroupDreamViewSet)
router.register(r'dreams', DreamViewSet)
router.register(r'frames', FrameViewSet)
router.register(r'packs', PackViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'usedcoupons', UsedCouponViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'paymentmethods', PaymentMethodViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'logs', LogViewSet)
router.register(r'wishlists', WishListViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'users', UserViewSet)
router.register(r'groupsusers', GroupUserViewSet)

admin.autodiscover()

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
