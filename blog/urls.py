from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("eco/<str:param>/",views.eco),
    path("json",views.api_info)
]