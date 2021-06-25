"""electromotive_force URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from calc import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('mean-deviation-calculator/',views.mean_deviation,name="mean_deviation"),
    path('average-calculator/',views.average,name="average"),
    path('pearson-correlation-calculator/',views.pearson_correlation,name="pearson_correlation"),
    path('linear-correlation-cofficient-calculator/',views.linear,name="linear"),
    path('zscore-calculator/',views.zscore,name="zscore"),
    path('descriptive-statistics-calculator/',views.descriptive_statistics,name="descriptive_statistics"),
    path('odds-probability-calculator/',views.oddsprob,name="oddsprob"),
    path('standard-deviation-calculator/',views.standarddeviation,name="standarddeviation"),
    path('statistics-formulas-calculator/',views.statisticsformulas,name="statisticsformulas"),
]
