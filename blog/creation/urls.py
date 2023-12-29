from django.urls import path
from . import views


app_name = 'creation'

urlpatterns = [
    path('creation_page/', views.CreateBlog.as_view(),  name='creation'),
    path('', views.Home.as_view(),  name='home_page'),
    path('edit_page/<int:blog_id>/', views.EditBlog.as_view(),  name='edit_page'),
    path('category_page/<int:category_id>/', views.CategoryView.as_view(),  name='category_page'),
    path('comment/', views.CommentView.as_view(), name='comment'),
]   