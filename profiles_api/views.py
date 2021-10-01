from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view """


    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_apiView = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to traditional Django views',
            'Gives you the most controll over your application logic',
            'is mapper manually to URLs ',
            'this message is added just for test'
        ]

        return Response({'message':'Hello!','api features': an_apiView})
