from django.urls import path
from . import views

app_name = 'authe'

urlpatterns = [
    path('signin/', views.Login.as_view(), name='login'),
    path('signup/', views.Register.as_view(), name='signup'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('delete/<int:blog_id>/', views.DeleteBlogView.as_view(), name = 'delete')
]