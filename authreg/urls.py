from django.urls import path
from authreg.views import RegisterView
from rest_framework.authtoken import views
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('api-token-auth/',views.obtain_auth_token),
]