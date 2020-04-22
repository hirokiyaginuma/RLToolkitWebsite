from django.shortcuts import render
from django.utils import timezone
from .models import Main, Post, Installing, Usage, Tutorials


def home(request):
    articles = Main.objects.filter(menu__contains='home').order_by('order')
    return render(request, 'website/home.html', {'articles':articles})
    
def installing(request):
    articles = Installing.objects.all().order_by('order')
    return render(request, 'website/installing.html', {'articles':articles})
    
def usage(request):
    articles = Usage.objects.all().order_by('order')
    return render(request, 'website/usage.html', {'articles':articles})

def tutorials(request):
    articles = Tutorials.objects.all().order_by('order')
    return render(request, 'website/tutorials.html', {'articles':articles})
    
def contact(request):
    articles = Main.objects.filter(menu__contains='contact').order_by('order')
    return render(request, 'website/contact.html', {'articles':articles})
    
def test(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'website/test.html', {'posts':posts})
