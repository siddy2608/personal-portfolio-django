from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extended user profile for portfolio owner"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Full Stack Developer")
    bio = models.TextField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    available_for_work = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Skill(models.Model):
    """Skills model"""
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & DevOps'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)  # 0-100
    icon = models.CharField(max_length=50, blank=True)  # Font Awesome class
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Projects model"""
    CATEGORY_CHOICES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile App'),
        ('ai', 'AI/ML'),
        ('api', 'API/Backend'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.ManyToManyField(Skill, related_name='projects')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    completed_date = models.DateField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-featured', '-completed_date', 'order']
    
    def __str__(self):
        return self.title


class Experience(models.Model):
    """Work experience model"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Skill, related_name='experiences')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='companies/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-current', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    """Education model"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-current', '-start_date']
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Certification(models.Model):
    """Certifications model"""
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
