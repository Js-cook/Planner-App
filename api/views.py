from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AssignmentSerializer

# Create your views here.
@api_view(["GET"])
def overview(request):
  urls = {
    "Retrieve Items": "/retrieve/",
    "Delete": "/delete/"
  }
  return Response(urls)