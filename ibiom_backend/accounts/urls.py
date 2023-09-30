from django.urls import path
from . views import *

urlpatterns = [
    path('register', UserRegistrationView.as_view(),name='register'),
    path('test', TestView.as_view(),name='test')
]