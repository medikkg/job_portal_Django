from django.db import models
from django.contrib.postgres.fields import ArrayField


class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_image = models.ImageField(upload_to='photos/countries/', default='photos/default_flag.jpg')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name


class JobPosition(models.Model):
    ONSITE = 'Onsite'
    REMOTE = 'Remote'
    HYBRYD = 'Hybryd'

    JOB_TYPE_CHOICES = [
        (ONSITE, 'Onsite'),
        (REMOTE, 'Remote'),
        (HYBRYD, 'Hybryd'),
    ]

    title = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    location = models.CharField(max_length=255)
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='job_positions')
    category = models.CharField(max_length=100) #added category
    designation = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)

    salary_min = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    experience = models.CharField(max_length=255)
    job_image = models.ImageField(upload_to='photos/job_images/%Y/%m/%d', blank=True, null=True, default='photos/default_flag.jpg')
    job_description = models.TextField()
    how_to_apply = models.TextField()
    job_requirements = models.TextField()
    skill = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default=ONSITE)



class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='photos/company_logos', blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.company_name