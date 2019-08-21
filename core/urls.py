from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('partner/', views.PartnerView.as_view(), name='partner'),
    path('program/', views.ProgramView.as_view(), name='program'),
    path('marker/', views.MarkerView.as_view(), name='marker'),
    path('district/', views.DistrictApi.as_view(), name='district'),
    path('province/', views.DistrictApi.as_view(), name='province'),
    path('gapanapa/', views.GapaNapaApi.as_view(), name='gapanapa'),
    path('fivew/', views.Fivew.as_view(), name='fivew'),

]
