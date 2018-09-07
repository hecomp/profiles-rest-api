from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, resquest, format=None):
        """Returns a list of APIview features."""

        an_apiview = [
            'Use HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        