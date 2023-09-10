from django.urls import path, include
from .views import listblogs, blogdetails

urlpatterns = [
    path('', listblogs, name='blogs'), #website.com/blog/,
    path('blogdetails/', blogdetails, name='blog_detail') #website.com/blog/adsasd3we23432432424rewfwe-sdfsdf
]
