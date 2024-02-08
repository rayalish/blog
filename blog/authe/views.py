from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from authe.models import User
from creation.models import Blog, Category




# Create your views here.
class Register(View):
    def get(self, request):
        form = UserSignUpForm()
        context = {
            'title': 'Регистрация',
            'form': form
        }
        return render(request, 'authe/index.html', context=context)
    
    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('authe:login'))
        else:
            context = {
                'form': form
            }
            return render(request, 'authe/index.html', context=context)
        
@method_decorator(login_required, name='get')



class Profile(LoginRequiredMixin, View):
    login_url = '/authe/signin/'
    
    def get(self, request):
        blogs_correct = Blog.objects.filter(author=request.user).order_by('-publish_date')
        blog_cnt = Blog.objects.filter(author=request.user).count()
        context = {
            'blogs_correct': blogs_correct,
            'blog_cnt': blog_cnt,
            'title': 'Профиль',
            
        }
        return render(request, 'authe/profile.html', context = context)
    




class Login(View):
    def get(self, request):
        form = UserSignInForm()
        context = {
            'title': 'Авторизация',
            'form': form
        }

        return render(request, 'authe/signin.html', context=context)
    
    def post(self, request):
        form = UserSignInForm(request, request.POST)

        if form.is_valid():
            try:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'],)
                login(request, user)
                return redirect(reverse_lazy('creation:home_page'))
            except:
                return render(request, 'authe/signin.html', context={'form': form, 'err': '1'})
        else:
            return render(request, 'authe/signin.html', context={'form': form, 'err': 2})
    
def signout(request):
    logout(request)
    return redirect(reverse_lazy('creation:home_page'))

class DeleteBlogView(View):
    def get(self, request, blog_id):
        movie = Blog.objects.get(id=blog_id)
        movie.delete()

        return redirect(reverse_lazy('authe:profile'))
    
class SearchProfileView(View):
    
    def get(self, request):
        form = SearchProfileForm()
        query = request.GET.get('q')
        if query:
            blogs_correct = Blog.objects.filter(author=request.user, title__icontains=query).order_by('-publish_date')
            if blogs_correct:
                context = {
                    'title': 'Поиск',
                    'form': form,
                    'blogs_correct': blogs_correct,
                    'query': query
                }
                return render(request, 'authe/search_profile.html', context=context)
            else:
                context = {
                    'title': 'Поиск',
                    'txt': 'По вашему запросу ничего не найдено',
                }
                return render(request, 'authe/search_profile.html', context=context)
        else:
            context = {
                'title': 'Поиск',
                'txt': 'Пожалуйста, введите ключевые слова для поиска',
            }
            return render(request, 'authe/search_profile.html', context=context)