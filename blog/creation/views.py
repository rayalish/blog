from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from .forms import *
from .models import *

class Home(View):
    def get(self, request):
        creation = Blog.objects.order_by('-publish_date')
        category = Category.objects.all()

        context = {
            'title': 'Все блоги',
            'creation': creation,
            'category': category,

        }

        return render(request, 'creation/home_page.html', context=context)

class Detail(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        comments = Comment.objects.filter(blog_id=blog_id)

        context = {
            'title': blog.title,
            'blog': blog,
            'comments': comments,
        }

        return render(request, 'creation/detail.html', context=context)


class CreateBlog(View):
    def get(self, request):
        form = BlogCreationForm()

        context = {
            'title': 'Создать блог',
            'form': form,
        }

        return render(request, 'creation/creation_page.html', context=context)
    
    def post(self, request):
        form = BlogCreationForm(request.POST, request.FILES)

        if form.is_valid():
            current_user = request.user
            
            blog_instance = form.save(commit=False)
            blog_instance.author = current_user
            blog_instance.save()
            return redirect(reverse_lazy('creation:home_page'))
        else:
            context = {
                'title': 'Создать блог',
                'form': form,
                'error': 1,
            }

            return render(request, 'creation/creation_page.html', context=context)
        
class SearchBlogView(View):
    def get(self, request):
        form = SearchForm()
        query = request.GET.get('q')
        category = Category.objects.all()
        if query:
            creation = Blog.objects.filter(title__icontains=query).order_by('-publish_date')
            if creation:
                context = {
                    'title': 'Поиск',
                    'form': form,
                    'creation': creation,
                    'category': category,
                    'query': query
                }
                return render(request, 'creation/search_results.html', context=context)
            else:
                context = {
                    'title': 'Поиск',
                    'txt': 'По вашему запросу ничего не найдено',
                    'category': category,
                }
                return render(request, 'creation/search_results.html', context=context)
        else:
            context = {
                'title': 'Поиск',
                'txt': 'Пожалуйста, введите ключевые слова для поиска',
                'category': category,
            }
            return render(request, 'creation/search_results.html', context=context)
            
        
    
class EditBlog(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        form = BlogCreationForm(blog.to_json())

        context = {
            'title': 'Редактировать фильм',
            'form': form,
            'blog': blog,
        }

        return render(request, 'creation/edit_page.html', context=context)
    
    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        form = BlogCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                blog.image = request.FILES['image']
            
            blog.title = request.POST['title']
            blog.description = request.POST['description']
            blog.category = Category.objects.get(id=request.POST['category'])
            
            blog.save()
            return redirect(reverse_lazy('creation:home_page'))
        else:
            context = {
                'title': 'Редактировать блог',
                'form': form,
                'blog': blog,
                'error': 1,
            }
            return render(request, 'creation/edit_page.html', context=context)
        
class CategoryView(View):
    def get(self, request, category_id):

        category = Category.objects.all()

        selected_category = Category.objects.get(pk=category_id)

        blogs_in_category = Blog.objects.filter(category=selected_category).order_by('-publish_date')
        

        context = {
            'title': f'Категория: {selected_category.name}',
            'selected_category': selected_category,
            'blogs_in_category': blogs_in_category,
            'category': category
        }

        return render(request, 'creation/category_page.html', context=context)  
    

    
class CommentView(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
            
        blog_id = data.get('blog_id')
        text = data.get('text')
        user_id = data.get('user_id')

        blog = Blog.objects.get(id=blog_id)
        user = User.objects.get(id=user_id)
        
        comment = Comment.objects.create(
            text=text,
            author=user,
            blog=blog
        )        
        comment.save()
        
        return HttpResponse({'data': 'success'})
    
