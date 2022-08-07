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
    if assignment.dt.date() == datetime.date(year, month, day):
      serializer = AssignmentSerializer(assignment)
      assignments.append(serializer.data)
  return Response(assignments)

@api_view(["GET"])
def get_month_assignments(request, month, year):
  assignments = []
  for assignment in list(Assignment.objects.all()):
    if assignment.dt.month() == datetime.datetime(year, month, 1).month() and assignment.dt.year() == datetime.datetime(year, month, 1).year():
      serializer = AssignmentSerializer(assignment)
      assignments.append(serializer.data)
  return Response(assignments)

@api_view(["GET"])
def update_status(request, id):
  assignment = Assignment.objects.get(id=id)
  assignment.completed = True
  return Response("Assignment Completed")

@api_view(["POST"])
def create_assignment(request):
  data = request.data
  dt_obj = datetime.datetime.fromtimestamp(data["dt"]//1000)
  serializer = AssignmentSerializer(data={"title":data['title'], "description":data["description"], "dt":dt_obj, "type":data['type']})
  if serializer.is_valid():
    serializer.save()
    return Response("Assignment created successfully")
  else:
    return Response("Something went wrong...")
