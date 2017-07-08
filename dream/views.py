from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Group, Dream, Frame, Library, Pack
from .serializers import GroupSerializer, DreamSerializer, FrameSerializer, LibrarySerializer, PackSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DreamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dream to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated, )

    queryset = Dream.objects.all()
    serializer_class = DreamSerializer


class FrameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frame to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Frame.objects.all()
    serializer_class = FrameSerializer


class PackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Pack.objects.all()
    serializer_class = PackSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
