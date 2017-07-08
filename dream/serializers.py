from rest_framework import serializers
from .models import Group, Dream, Frame, Library, Pack


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'is_available')


class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ('id', 'is_available', 'duration', 'image_source', 'image_back_source', 'image_repetition', 'text', 'text_repetition', 'dream')


class DreamSerializer(serializers.ModelSerializer):
    frames = FrameSerializer(many=True, read_only=True)

    class Meta:
        model = Dream
        fields = ('id', 'name', 'description', 'introduction', 'cover_page', 'is_available', 'price', 'alarm_sound', 'alarm_time',
                  'alarm_duration', 'alarm_repetition', 'dream_sound', 'group', 'android_code', 'ios_code', 'frames')


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = ('id', 'name', 'description', 'is_available', 'price', 'dreams', 'groups', 'android_code', 'ios_code')


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'user', 'dream', 'pack')
