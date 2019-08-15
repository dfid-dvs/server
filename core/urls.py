from django.contrib import admin
from django.urls import path,include
from core import views

def trigger_error(request):
    division_by_zero = 1 / 1
    return int(division_by_zero)

urlpatterns = [
    path('test/', trigger_error,name='test'),
    path('organization/', views.OrganizationView.as_view(),name='organization'),
    path('program/', views.ProgramView.as_view(),name='program'),
    path('marker/', views.MarkerView.as_view(),name='marker'),
]
