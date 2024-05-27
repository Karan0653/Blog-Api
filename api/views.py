from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serialisers import *
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Register':'/register/',
        'Login':'/login/',
        'Profile':'/profile/',
        'Blogs' : '/blog/',
        'Blog_detail':'/blog/<str:pk>/',
        'Create_blog' : '/create/',
        'Update_blog' : '/update/',
        'User_data' : '/user_data/',
        'Delete_blog': '/delete/<str:pk>/',
        'Profile_update' : '/profile_update/'
          
    }

    return Response(api_urls)

@api_view(['POST'])
def register(request):

    print(request.data)
    user = request.data

    username = user['username']
    password = user['password']
    email = user['email']

    if User.objects.filter(username=username).exists():
        return Response('Username already exists')
    
    if User.objects.filter(email = email).exists():
        return Response('Email already exists')

    if username and password and email:
        user_obj = User.objects.create_user(username=username,password=password,email=email)
        user_obj.save()
        Author.objects.create(user=user_obj,name=username)

        return Response('Registration Successful')
    
    return Response('failed')
 
# 1092847 q@ hello

@api_view(['PUT'])
def loginPage(request):
    user = request.data
    username = user['name']
    password = user['password']

    if username and password:
         user_obj = authenticate(request, username=username, password=password)

         if user_obj is not None:
            # print(user_obj)
            # print(user_obj.id)
            user_id = user_obj.id
            return Response(user_id,status=status.HTTP_200_OK)
    return Response('Invalid Crendentials!',status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def blog(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    # print(serializer.data)
    if serializer:
        return Response(serializer.data)
    return Response('No Blogs to be found')


@api_view(['GET'])
def blog_detail(request, pk):
    blog = Blog.objects.get(id = pk)

    serializer = BlogSerializer(blog, many=False)
     
    author_id = serializer.data['written_by']
    author = Author.objects.get(id = author_id)

    author_serializer = AuthorSerializer(author, many = False)
    # print('author_serializer',author_serializer.data)

    author_name = author_serializer.data['name']
    print(author_name)
   
    serializer.data['author_name'] = author_name
    d = serializer.data

    d['author_name'] = author_name
    # print(d)

    return Response(d)


@api_view(['POST'])
def createBlog(request):
    print(request.data)

    blog_form_data = request.data

    title = blog_form_data['title']
    content = blog_form_data['content']
    author = blog_form_data['author']

    # author_obj = Author.objects.get(name=author)
    # author_serialised = AuthorSerializer(author_obj)
    # print(author_serialised.data)

    # author_id = author_serialised.data['id']
    created = Blog.objects.create(title=title,content=content,written_by= Author.objects.get(name=author))

    if created:
        return Response('Created!')
    
    return Response('Could not create blog :(')

@api_view(['POST'])
def profile(request):
    name = request.data
    print(name)
    author = Author.objects.get(name = name)
    print(author)

    blogs = author.blog_set.all()
    
    if blogs:
        blog_serialised = BlogSerializer(blogs, many=True )
        
        return Response(blog_serialised.data)
    
    return Response([],status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def profile_update(request):
    name = request.data['name']
    desc = request.data['desc']
    author = Author.objects.get(name = name)

    author.description = desc
    author.save()

    print(request.data)
    return Response('Description Updated!!!')

@api_view(['GET'])
def user_data(request, pk):
    user = User.objects.get(id = pk)
    author = Author.objects.get(name = user)
    author_serialised = AuthorSerializer(author, many=False)
    print(author_serialised.data)
    return Response(author_serialised.data)



@api_view(['POST'])
def update_blog(request):
    blog = request.data
    # print(request.data)


    title = blog['title']
    content = blog['content']
    blog_id = blog['id']
    blog_obj = Blog.objects.get(id = blog_id)
    # print('blog_obj',blog_obj)

    blog_obj.title = title
    blog_obj.content = content

    blog_obj.save()
    return Response('updated!')


@api_view(['DELETE'])
def delete_blog(request, pk):
    blog_obj = Blog.objects.get(id = pk)
    blog_obj.delete()

    return Response('Successfully deleted')
 
