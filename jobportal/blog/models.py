import uuid
from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     category_name = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self) -> str:
#         return self.category_name


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/', default='photos/blogs/newsdef.jpg', null=True,
                              blank=True, )
    # categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_at']  # Сортировка в обратную сторону в зав-ти от создания новости

    def __str__(self) -> str:
        return self.title



