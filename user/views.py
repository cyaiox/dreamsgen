from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Profile, Address, Log, WishList, Experience
from .serializers import ProfileSerializer, AddressSerializer, LogSerializer, \
                         WishListSerializer, ExperienceSerializer, UserSerializer, GroupSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dream to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class LogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frame to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Log.objects.all()
    serializer_class = LogSerializer


class WishListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pack to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be created, viewed, edited or deleted.
    """
    permission_classes = (IsAuthenticated,)
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LoginView(APIView):
    """
    Post: Log user into the system
    """
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        #print request.data.get('username') + ' ' + \
        #      request.data.get('password')
        user = authenticate(username=request.data.get('username'),
                            password=request.data.get('password'))
        
        if user is not None and user.is_active:
            login(request, user)
            data = UserSerializer(user).data

            return Response(data, status.HTTP_200_OK)
        else:
            return Response({'error': 'Incorrect username/password.'}, status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    Get: Log user out of the system
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({}, status.HTTP_200_OK)
