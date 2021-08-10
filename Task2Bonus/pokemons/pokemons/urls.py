"""pokemons URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('type1/', views.type1),
    path('type2/', views.type2),
    path('type3/', views.type3),
    path('type4/', views.type4),
    path('type5/', views.type5),
    path('type6/', views.type6),
    path('type7/', views.type7),
    path('type8/', views.type8),
    path('type9/', views.type9),
    path('type10/', views.type10),
    path('type11/', views.type11),
    path('type12/', views.type12),
    path('type13/', views.type13),
    path('type14/', views.type14),
    path('type15/', views.type15),
    path('type16/', views.type16),
    path('type17/', views.type17),
    path('type18/', views.type18),
]
