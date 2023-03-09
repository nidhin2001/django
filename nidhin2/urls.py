from django.urls import path
from .view import registerview, LoginView,Userview,logoutview

urlpatterns = [
    path('register',registerview.as_view()),
    path('login', LoginView.as_view()),
path('user', Userview.as_view()),
path('logout', logoutview.as_view())
]