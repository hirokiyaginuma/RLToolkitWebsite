from django.shortcuts import render
from django.utils import timezone
from .models import Post



def home(request):
    return render(request, 'website/home.html', {})
    
def test(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/test.html', {'posts':posts})
