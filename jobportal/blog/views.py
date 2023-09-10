from django.shortcuts import render
# from .models import Blog, Category

# topRecentNews = Blog.objects.order_by('-created_at')[:3]
# categories = Category.objects.all()

def listblogs(request):
    # allNews = Blog.objects.all()
    # content = {
    #     'allNews': allNews,
    #     'topRecentNews': topRecentNews,
    #     'categories': categories,
    # }
    return render(request, 'blog/blogs.html',)

def blogdetails(request, blog_id):
    # blog = Blog.objects.get(id = blog_id)
    # comments = blog.comments.all()
    # context = {
    #     'blog': blog,
    #     'topRecentNews': topRecentNews,
    #     'categories': categories,
    # }
    return render(request, 'blog/blog_details.html',)