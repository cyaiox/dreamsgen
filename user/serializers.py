from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Profile, Address, Log, WishList, Experience


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'plan', 'identification_type', 'identification_number', 'birth_date', 'sex',
                  'phone_number', 'is_mark')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('pk', 'user', 'street', 'city', 'state', 'postal_code', 'country')


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('pk', 'user', 'date', 'ip', 'browser_fingerprint')


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('pk', 'user', 'dream', 'pack')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('pk', 'user', 'dream', 'date', 'text')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'email')

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'name')
