from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

def index(request: Request) -> Response:
    return Response(status=status.HTTP_200_OK, data=request.data)
