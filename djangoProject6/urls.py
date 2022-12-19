"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from caps.views import *
from rest_framework.routers import SimpleRouter
from users.urls import urlpatterns as user_urls
from .swagger import urlpatterns as swagger_urls

router = SimpleRouter()
router.register(r'cap', CapViewSet)
router.register(r'order', OrderViewSet)
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main-menu/', MainMenuListAPIView.as_view()),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('brands/<int:id>/', BrandUpdateDeleteAPIView.as_view()),
    path('categories/<int:id>/', CategoryUpdateDeleteAPIView.as_view()),
] + router.urls + user_urls + swagger_urls
