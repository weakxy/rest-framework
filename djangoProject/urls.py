"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^(?P<version>[v1|2]+)/dog/$', views.DogView.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/order/$', views.OrderPayment.as_view()),
    # path('dog/', views.DogView.as_view()),
    # path('order/', views.OrderPayment.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/urls/view/$', views.UsersView.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/parser/view/$', views.ParserView.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/serializers/view/$', views.SerializersView.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/serializersverify/view/$', views.SerializerVerify.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/serializers2/view/(?P<pk>\d+)/$', views.Serializers2View.as_view(), name='gp'),
    re_path(r'^(?P<version>[v1|2]+)/pager/view/$', views.PagerView.as_view()),
    re_path(r'^(?P<version>[v1|2]+)/view/$', views.View.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'^(?P<version>[v1|2]+)/view/(?P<pk>\d+)/$',
            views.View.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
]
