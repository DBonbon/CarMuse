from django.urls import path
from . import views
from about.views import AboutUs, AboutPageDetailView

urlpatterns = [
    path('',AboutUs.as_view(),name="about"),
    # path('<int:id>/', AboutPageDetailView.as_view(), name="about"),
]
