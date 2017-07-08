from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Group, Audio
from .serializers import GroupSerializer, AudioSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AudioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Audio.objects.all()
    serializer_class = AudioSerializer