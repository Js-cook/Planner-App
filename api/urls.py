from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.overview, name="overview"),
    path("get-assignments/<int:year>/<int:month>/<int:day>/", views.get_assignments, name="fetch-assi"),
    path("update-status/<int:id>/", views.update_status, name="update status"),
    path("new-assignment/", views.create_assignment, name="create assignment"),
    path("get-month-assignments/<int:month>/<int:year>/", views.get_month_assignments, name="month assignments")
]