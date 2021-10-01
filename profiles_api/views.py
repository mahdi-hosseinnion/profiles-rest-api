from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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
