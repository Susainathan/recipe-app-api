from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('token/', views.CreateToken.as_view(), name='token'),

]
