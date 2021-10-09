from django.urls import path
from .views import RegisterView,VerifyEmail,LoginAPIView


urlpatterns=[
    path('v1/register/',RegisterView.as_view(),name='register'),
    path('v1/login/', LoginAPIView.as_view(),name = 'login'),
    path('v1/email-verify/',VerifyEmail.as_view(),name='email-verify')

]

