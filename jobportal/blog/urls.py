from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', listblogs, name='blogs'), #website.com/blog/,
    path('<str:blog_id>', blogdetails, name='blog_details'),
    path('category/<int:category_id>', blog_by_category, name='blogs_by_cat')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)