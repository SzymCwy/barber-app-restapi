"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from salon.views import visit_create, visit_list, visit_update, visit_detail, service_list, service_create, \
    service_update, service_detail, UserList, UserDetail, UserCreate, UserUpdate, MyProfile, My_Visits, VerifyMail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', service_list.as_view()),
    path('services/<int:pk>/', service_detail.as_view()),
    path('services/create/', service_create.as_view()),
    path('services/<int:pk>/update/', service_update.as_view()),
    path('visits/', visit_list.as_view()),
    path('visits/create/', visit_create.as_view()),
    path('visits/<int:pk>/update/', visit_update.as_view()),
    path('visits/<int:pk>/', visit_detail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/<int:pk>/update/', UserUpdate.as_view()),
    path('users/create/', UserCreate.as_view()),
    path('profile/', MyProfile.as_view()),
    path('myvisits/', My_Visits.as_view()),
    path('verify/', VerifyMail.as_view()),
]
