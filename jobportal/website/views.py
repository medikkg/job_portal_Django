from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about-us.html')


def companies(request):
    return render(request, 'website/companies.html')


def contact(request):
    return render(request, 'website/contact.html')


def browse_job_list(request):
    return render(request, 'website/browse-job-list.html')

def all_jobs(request):
    return render(request, 'website/category-all-jobs.html')


def category_company_jobs(request):
    return render(request, 'website/category-company-jobs.html')

def category_designations_jobs(request):
    return render(request, 'website/category-designations-jobs.html')


def category_jobs(request):
    return render(request, 'website/category-jobs.html')


def register_2(request):
    return render(request, 'website/register-2.html')