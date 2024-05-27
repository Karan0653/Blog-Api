from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='apiOverView'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('profile/',views.profile,name='profile'),
    path('blog/',views.blog,name='blog'),
    path('blog/<str:pk>/',views.blog_detail,name='blog_detail'),
    path('create/',views.createBlog,name='create_blog'),
    path('update/',views.update_blog,name='update'),
    path('user_data/<str:pk>/',views.user_data,name='user_data'),
    path('delete/<str:pk>/',views.delete_blog,name='delete'),
    path('profile_update/',views.profile_update,name='profile_update')
]
