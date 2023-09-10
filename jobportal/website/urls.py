from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('companies/', views.companies, name='companies'),
    path('browse-job-list/', views.browse_job_list, name='browse_job_list'),
    path('all-jobs/', views.all_jobs, name='category_all_jobs'),
    path('category-jobs/', views.category_jobs, name='category_jobs'),
    path('category-designations-jobs/', views.category_designations_jobs, name='category_designations_jobs'),
    path('category-company-jobs/', views.category_company_jobs, name='category_company_jobs'),
    path('register-2/', views.register_2, name='register_2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)