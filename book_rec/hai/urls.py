from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('genres/', views.genres, name='genres'),
    path('genres/<str:genre_name>/', views.genre_books, name='genre_books'),
   
]
