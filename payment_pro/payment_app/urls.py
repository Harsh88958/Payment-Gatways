from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path("", views.index),
    path("create/", create, name="create_payment"),
    path("paypage/", paypage, name="paypage"),
]
