from django.shortcuts import render
from django.utils import timezone
from .models import Post, Installing, Tutorials


def home(request):
    return render(request, 'website/home.html', {})
    
def installing(request):
    articles = Installing.objects.all().order_by('order')
    return render(request, 'website/installing.html', {'articles':articles})

def tutorials(request):
    articles = Tutorials.objects.all().order_by('order')
    return render(request, 'website/tutorials.html', {'articles':articles})
    
def contact(request):
    return render(request, 'website/contact.html', {})
    
def test(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'website/test.html', {'posts':posts})
