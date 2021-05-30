"""askme_turchin URL Configuration

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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('question/<int:pk>/', views.question, name='question'),
    path('popular/', views.popular_questions),
    path('ask/', views.ask),
    path('login/', views.login),
    path('signup/', views.reg),
    path('tag/', views.tag_search),
    path('user/', views.user),
    # path(r'^page/(\+d)/$', views.index_page)
    # path('page/<int:pk>', views.index_page)
    # path('', views.)
]
