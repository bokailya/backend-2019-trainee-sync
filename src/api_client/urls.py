from django.urls import path

from api_client import views

urlpatterns: list = [
    path('account', views.AccountView.as_view(), name='account'),
    path('ticket', views.TicketMobileView.as_view(), name='ticket'),
    path('recognize', views.RecognizeView.as_view(), name='recognize'),
    path('signIn', views.SignInView.as_view(), name='sign_in'),
    path('signUp', views.SignUpView.as_view(), name='sign_up'),
]
