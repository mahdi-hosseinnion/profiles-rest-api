from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test api view """

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiView = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to traditional Django views',
            'Gives you the most controll over your application logic',
            'is mapper manually to URLs ',
            'this message is added just for test'
        ]

        return Response({'message':'Hello!','api features': an_apiView})


    def post(self, requset):
        """Create hellow mesage with out name"""
        serializer = self.serializer_class(data = requset.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} you are a cool guy'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, requst, pk = None):
        """Update a object"""
        return Response({'method': 'put'})

    def patch(self, requst, pk = None):
        """Update a partial part of object"""
        return Response({'method': 'patch'})

    def delete(self, requst, pk = None):
        """Delete a object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Return a hello message"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a list of viewset features"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, delete)',
            'Automatilly maps to URLs using Routers',
            'Provide more functionality with less code',
        ]

        return Response({'message':'Hello i am a viewSet','features':a_viewset})

    def create(self, request):
        """Create new hello message with user name in it"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}! what is up?'

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """Handle retrieving a specific object"""

        return Response({'HTTP_METHOD':'GET'})

    def update(self, request, pk = None):
        """Handle updating a specific object"""

        return Response({'HTTP_METHOD':'PUT'})

    def partial_update(self, request, pk = None):
        """Handle update a partial section of a specific object"""

        return Response({'HTTP_METHOD':'PATCH'})

    def destroy(self, request, pk = None):
        """Handle removing a specific object"""

        return Response({'HTTP_METHOD':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class            = serializers.UserProfileSerializer
    queryset                    = models.UserProfile.objects.all()
    authentication_classes      = (TokenAuthentication, )
    permission_classes          = (permissions.UpdateOwnProfile, )
    filter_backends             = (filters.SearchFilter, )
    search_fields               = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes            = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profile feed items"""
    authentication_classes      = (TokenAuthentication, )
    serializer_class            = serializers.ProfileFeedItemSerializer
    queryset                    = models.ProfileFeedItem.objects.all()
    permission_classes          = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        """Sets user profile to logged user"""
        serializer.save(user_profile = self.request.user)
