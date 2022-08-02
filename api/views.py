from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AssignmentSerializer
from .models import Assignment

import datetime

# Create your views here.
@api_view(["GET"])
def overview(request):
  urls = {
    "Retrieve Items": "/retrieve/",
    "Delete": "/delete/"
  }
  return Response(urls)

@api_view(["GET"])
def get_assignments(request, year, month, day):
  assignments = []
  for assignment in list(Assignment.objects.all()):
    print(assignment.dt.date())
    print(datetime.date(year, month, day))
    if assignment.dt.date() == datetime.date(year, month, day):
      serializer = AssignmentSerializer(assignment)
      assignments.append(serializer.data)
  return Response(assignments)

@api_view(["GET"])
def update_status(request, id):
  assignment = Assignment.objects.get(id=id)
  assignment.completed = True
  return Response("Assignment Completed")

