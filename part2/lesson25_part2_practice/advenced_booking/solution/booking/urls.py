"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("destination/", views.DestinationListView.as_view()),
    path("destination/<int:pk>/", views.DestinationDetailView.as_view()),
    path("destination/create/", views.DestinationCreateView.as_view()),
    path("destination/<int:pk>/update/", views.DestinationUpdateView.as_view()),
    path("destination/<int:pk>/delete/", views.DestinationDeleteView.as_view()),
]