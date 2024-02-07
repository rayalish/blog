from django.urls import path
from . import views


app_name = 'creation'

urlpatterns = [
    path('creation_page/', views.CreateBlog.as_view(),  name='creation'),
    path('', views.Home.as_view(),  name='home_page'),
    path('edit_page/<int:blog_id>/', views.EditBlog.as_view(),  name='edit_page'),
    path('category_page/<int:category_id>/', views.CategoryView.as_view(),  name='category_page'),
    path('comments/', views.CommentView.as_view(), name='comment'),
    path('search/', views.SearchBlogView.as_view(), name='search'),
    path('detail/<int:blog_id>/', views.Detail.as_view(),  name='detail'),
]   