from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Profile, Skill, Project, Experience, Education, Certification, Contact
from .services import NotificationService
import json


def index(request):
    """Home page view"""
    context = {
        'profile': Profile.objects.first(),
        'featured_projects': Project.objects.filter(featured=True)[:3] if Project.objects.filter(featured=True).exists() else [],
        'skills': Skill.objects.filter(featured=True)[:8] if Skill.objects.filter(featured=True).exists() else [],
        'project_count': Project.objects.count(),
        'certification_count': Certification.objects.count(),
    }
    return render(request, 'core/index.html', context)


def about(request):
    """About page view"""
    context = {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'certifications': Certification.objects.all(),
    }
    return render(request, 'core/about.html', context)


def projects(request):
    """Projects page view"""
    projects_list = Project.objects.all()
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category and category != 'all':
        projects_list = projects_list.filter(category=category)
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        projects_list = projects_list.filter(
            title__icontains=search
        ) | projects_list.filter(
            description__icontains=search
        )
    
    context = {
        'projects': projects_list,
        'categories': Project.CATEGORY_CHOICES,
        'selected_category': category,
        'search_term': search,
    }
    return render(request, 'core/projects.html', context)


def project_detail(request, pk):
    """Individual project detail view"""
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'core/project_detail.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save contact submission
        contact_obj = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send notifications
        try:
            notification_result = NotificationService.send_contact_notifications(contact_obj)
            
            if notification_result['success']:
                messages.success(request, 'Thank you for your message! I will get back to you soon. You should receive a confirmation email shortly.')
            else:
                messages.warning(request, 'Thank you for your message! I will get back to you soon. (Note: Notification delivery may be delayed)')
                
        except Exception as e:
            # Log the error but don't show it to the user
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to send notifications: {str(e)}")
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
        
        return redirect('contact')
    
    context = {
        'profile': Profile.objects.first(),
    }
    return render(request, 'core/contact.html', context)


@login_required
def dashboard(request):
    """Dashboard view for contact statistics"""
    # Get date ranges
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    # Contact statistics
    total_contacts = Contact.objects.count()
    unread_contacts = Contact.objects.filter(is_read=False).count()
    today_contacts = Contact.objects.filter(created_at__date=today).count()
    week_contacts = Contact.objects.filter(created_at__date__gte=week_ago).count()
    month_contacts = Contact.objects.filter(created_at__date__gte=month_ago).count()
    
    # Recent contacts
    recent_contacts = Contact.objects.all()[:10]
    
    # Contact trends (last 7 days)
    daily_contacts = []
    for i in range(7):
        date = today - timedelta(days=i)
        count = Contact.objects.filter(created_at__date=date).count()
        daily_contacts.append({
            'date': date.strftime('%b %d'),
            'count': count
        })
    daily_contacts.reverse()
    
    context = {
        'total_contacts': total_contacts,
        'unread_contacts': unread_contacts,
        'today_contacts': today_contacts,
        'week_contacts': week_contacts,
        'month_contacts': month_contacts,
        'recent_contacts': recent_contacts,
        'daily_contacts': daily_contacts,
    }
    return render(request, 'core/dashboard.html', context)


# API Views for dynamic content
@csrf_exempt
def api_skills(request):
    """API endpoint for skills"""
    skills = Skill.objects.all().values(
        'id', 'name', 'category', 'proficiency', 'icon', 'featured'
    )
    return JsonResponse(list(skills), safe=False)


@csrf_exempt
def api_projects(request):
    """API endpoint for projects"""
    projects = Project.objects.all().values(
        'id', 'title', 'description', 'category', 
        'github_url', 'live_url', 'featured', 'completed_date'
    )
    return JsonResponse(list(projects), safe=False)
