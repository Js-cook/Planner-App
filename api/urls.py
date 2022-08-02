from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.overview, name="overview"),
    path("get-assignments/<int:year>/<int:month>/<int:day>/", views.get_assignments, name="fetch-assi")
]