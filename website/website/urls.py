"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from apidemo import views
from django.conf.urls.static import static



# import apidemo.views

urlpatterns = [
	url(r'^$', views.index),  # new
    url(r'^admin/', admin.site.urls),
	url(r'^stocks/', views.StockList.as_view()),
	url(r'^music/', include('music.urls')),
	#url(r'^abc/', views.ABCList.as_view()),cd
]

urlpatterns = format_suffix_patterns(urlpatterns)