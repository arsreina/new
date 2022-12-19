from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
ACTIONS = {
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
    'update': 'update'
}

router = SimpleRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegistrationView.as_view(ACTIONS))
] + router.urls
