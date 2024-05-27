from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateBlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['date_posted','written_by']

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']