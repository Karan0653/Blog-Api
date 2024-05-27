from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length = 200, null = True)

    def __str__(self) -> str:
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length = 200, null = True)
    content = models.CharField(max_length = 5000, null = True)
    written_by = models.ForeignKey(Author, null=True, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self) -> str:
        return self.title
 


