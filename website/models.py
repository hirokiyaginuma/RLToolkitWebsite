from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

CHOICE = { ('home', 'Home'), ('contact', 'Contact')}
GET_CHOICE = { ('env', 'Initialize environment'), 
             ('method', 'Initialize method'), 
             ('callback', 'Choose callbacks'), 
             ('train', 'Train model'), 
             ('result', 'Show results') }

class Main(models.Model):
    menu = models.CharField(max_length=200, choices=CHOICE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='Sample Text')
    order = models.BigIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        
class GetStarted(models.Model):
    menu = models.CharField(max_length=200, choices=GET_CHOICE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='Sample Text')
    order = models.BigIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

        
class Installing(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='Sample Text')
    order = models.BigIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        
class Usage(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='Sample Text')
    order = models.BigIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        
class Tutorials(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='Sample Text')
    order = models.BigIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default='Sample Text')
    content = RichTextUploadingField(default='Sample Text')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title