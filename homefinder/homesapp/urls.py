from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('<pk>',views.LocationView.as_view(), name="property"),
    path('<int:locationid>/<pk>',views.PropertyDetail.as_view(), name="propertyview"),
]

