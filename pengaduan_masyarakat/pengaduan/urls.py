"""
URL configuration for pengaduan_masyarakat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # Masyarakat
    path('masyarakat/', views.masyarakat_list, name='masyarakat_list'),
    path('masyarakat/create/', views.masyarakat_create, name='masyarakat_create'),
    path('masyarakat/update/<int:pk>/', views.masyarakat_update, name='masyarakat_update'),
    path('masyarakat/delete/<int:pk>/', views.masyarakat_delete, name='masyarakat_delete'),

    # Petugas
    path('petugas/', views.petugas_list, name='petugas_list'),
    path('petugas/create/', views.petugas_create, name='petugas_create'),
    path('petugas/update/<int:pk>/', views.petugas_update, name='petugas_update'),
    path('petugas/delete/<int:pk>/', views.petugas_delete, name='petugas_delete'),

    # Pengaduan
    path('pengaduan/', views.pengaduan_list, name='pengaduan_list'),
    path('pengaduan/create/', views.pengaduan_create, name='pengaduan_create'),
    path('pengaduan/update/<int:pk>/', views.pengaduan_update, name='pengaduan_update'),
    path('pengaduan/delete/<int:pk>/', views.pengaduan_delete, name='pengaduan_delete'),

    # Tanggapan
    path('tanggapan/', views.tanggapan_list, name='tanggapan_list'),
    path('tanggapan/create/', views.tanggapan_create, name='tanggapan_create'),
    
]


