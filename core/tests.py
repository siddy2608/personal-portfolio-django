from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from django.test.utils import override_settings
from django.utils import timezone
from datetime import date, timedelta
import json

from .models import Profile, Skill, Project, Contact, Education, Certification
from .forms import ContactForm, FileUploadForm


class ModelTests(TestCase):
    """Test cases for models"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.profile = Profile.objects.create(
            user=self.user,
            title='Test Developer',
            bio='Test bio',
            location='Test City',
            phone='+1234567890',
            available_for_work=True
        )
        
        self.skill = Skill.objects.create(
            name='Python',
            category='backend',
            proficiency=85,
            icon='fab fa-python',
            featured=True,
            order=1
        )
        
        self.project = Project.objects.create(
            title='Test Project',
            description='Test project description',
            category='web',
            github_url='https://github.com/test/project',
            live_url='https://test-project.com',
            featured=True,
            completed_date=date.today(),
            order=1
        )
        
        self.contact = Contact.objects.create(
            name='Test User',
            email='test@example.com',
            subject='Test Subject',
            message='Test message content'
        )
    
    def test_profile_creation(self):
        """Test profile creation and string representation"""
        self.assertEqual(str(self.profile), "testuser's Profile")
        self.assertEqual(self.profile.title, 'Test Developer')
        self.assertTrue(self.profile.available_for_work)
    
    def test_skill_creation(self):
        """Test skill creation and ordering"""
        self.assertEqual(str(self.skill), 'Python')
        self.assertEqual(self.skill.category, 'backend')
        self.assertEqual(self.skill.proficiency, 85)
        self.assertTrue(self.skill.featured)
    
    def test_project_creation(self):
        """Test project creation and relationships"""
        self.assertEqual(str(self.project), 'Test Project')
        self.assertEqual(self.project.category, 'web')
        self.assertTrue(self.project.featured)
        
        # Test many-to-many relationship
        self.project.technologies.add(self.skill)
        self.assertIn(self.skill, self.project.technologies.all())
    
    def test_contact_creation(self):
        """Test contact form submission creation"""
        self.assertEqual(str(self.contact), 'Message from Test User - Test Subject')
        self.assertFalse(self.contact.is_read)
        self.assertIsNotNone(self.contact.created_at)


class ViewTests(TestCase):
    """Test cases for views"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.profile = Profile.objects.create(
            user=self.user,
            title='Test Developer',
            bio='Test bio',
            location='Test City',
            phone='+1234567890'
        )
        
        self.skill = Skill.objects.create(
            name='Python',
            category='backend',
            proficiency=85,
            featured=True
        )
        
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            category='web',
            featured=True,
            completed_date=date.today()
        )
    
    def test_index_view(self):
        """Test home page view"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertIn('profile', response.context)
        self.assertIn('featured_projects', response.context)
        self.assertIn('skills', response.context)
    
    def test_about_view(self):
        """Test about page view"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
        self.assertIn('profile', response.context)
        self.assertIn('skills', response.context)
        self.assertIn('education', response.context)
    
    def test_projects_view(self):
        """Test projects page view"""
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/projects.html')
        self.assertIn('projects', response.context)
        self.assertIn('categories', response.context)
    
    def test_projects_filtering(self):
        """Test project filtering by category"""
        response = self.client.get(reverse('projects'), {'category': 'web'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['selected_category'], 'web')
    
    def test_projects_search(self):
        """Test project search functionality"""
        response = self.client.get(reverse('projects'), {'search': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'Test')
    
    def test_project_detail_view(self):
        """Test individual project detail view"""
        response = self.client.get(reverse('project_detail', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/project_detail.html')
        self.assertEqual(response.context['project'], self.project)
    
    def test_project_detail_404(self):
        """Test project detail view with invalid ID"""
        response = self.client.get(reverse('project_detail', args=[99999]))
        self.assertEqual(response.status_code, 404)
    
    def test_contact_view_get(self):
        """Test contact page GET request"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
        self.assertIn('profile', response.context)
    
    def test_contact_view_post_valid(self):
        """Test contact form submission with valid data"""
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message for contact form.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        # Check if contact was created
        contact = Contact.objects.get(email='test@example.com')
        self.assertEqual(contact.name, 'Test User')
        self.assertEqual(contact.subject, 'Test Subject')
    
    def test_contact_view_post_invalid(self):
        """Test contact form submission with invalid data"""
        data = {
            'name': '',  # Invalid: empty name
            'email': 'invalid-email',  # Invalid email
            'subject': 'Test',
            'message': 'Short'  # Too short
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)  # Stay on form page
    
    def test_dashboard_view_authenticated(self):
        """Test dashboard view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')
    
    def test_dashboard_view_unauthenticated(self):
        """Test dashboard view for unauthenticated user"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_api_skills(self):
        """Test skills API endpoint"""
        response = self.client.get(reverse('api_skills'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Python')
    
    def test_api_projects(self):
        """Test projects API endpoint"""
        response = self.client.get(reverse('api_projects'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Project')


class FormTests(TestCase):
    """Test cases for forms"""
    
    def test_contact_form_valid(self):
        """Test contact form with valid data"""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject Line',
            'message': 'This is a valid test message with sufficient length.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_contact_form_invalid_name(self):
        """Test contact form with invalid name"""
        form_data = {
            'name': 'J',  # Too short
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Valid message content.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
    
    def test_contact_form_invalid_email(self):
        """Test contact form with invalid email"""
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'subject': 'Test Subject',
            'message': 'Valid message content.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_contact_form_spam_detection(self):
        """Test contact form spam detection"""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Buy now! Click here for free money! Act now!'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)
    
    def test_file_upload_form_valid(self):
        """Test file upload form with valid file"""
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        file_content = b'Test file content'
        uploaded_file = SimpleUploadedFile(
            'test.txt',
            file_content,
            content_type='text/plain'
        )
        
        form_data = {'file': uploaded_file}
        form = FileUploadForm(
            data=form_data,
            allowed_types=['text/plain'],
            max_size=1024
        )
        self.assertTrue(form.is_valid())
    
    def test_file_upload_form_invalid_size(self):
        """Test file upload form with oversized file"""
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        # Create a file larger than the limit
        file_content = b'x' * 2048  # 2KB
        uploaded_file = SimpleUploadedFile(
            'test.txt',
            file_content,
            content_type='text/plain'
        )
        
        form_data = {'file': uploaded_file}
        form = FileUploadForm(
            data=form_data,
            allowed_types=['text/plain'],
            max_size=1024  # 1KB limit
        )
        self.assertFalse(form.is_valid())
        self.assertIn('file', form.errors)


class IntegrationTests(TestCase):
    """Integration test cases"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.profile = Profile.objects.create(
            user=self.user,
            title='Test Developer',
            bio='Test bio',
            location='Test City',
            phone='+1234567890'
        )
    
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_contact_form_email_notification(self):
        """Test complete contact form flow with email notification"""
        # Submit contact form
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message for integration testing.'
        }
        response = self.client.post(reverse('contact'), data)
        
        # Check if contact was created
        contact = Contact.objects.get(email='test@example.com')
        self.assertEqual(contact.name, 'Test User')
        
        # Check if emails were sent
        self.assertEqual(len(mail.outbox), 2)  # Notification + confirmation
        
        # Check notification email
        notification_email = mail.outbox[0]
        self.assertIn('New Contact Form Submission', notification_email.subject)
        self.assertEqual(notification_email.to[0], 'siddharthmishr125@gmail.com')
        
        # Check confirmation email
        confirmation_email = mail.outbox[1]
        self.assertIn('Thank you for contacting me', confirmation_email.subject)
        self.assertEqual(confirmation_email.to[0], 'test@example.com')
    
    def test_user_journey_home_to_contact(self):
        """Test complete user journey from home to contact"""
        # Visit home page
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
        # Visit about page
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        
        # Visit projects page
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        
        # Visit contact page
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        
        # Submit contact form
        data = {
            'name': 'Journey User',
            'email': 'journey@example.com',
            'subject': 'Journey Test',
            'message': 'Testing the complete user journey through the portfolio.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success


class PerformanceTests(TestCase):
    """Performance test cases"""
    
    def setUp(self):
        """Set up test data for performance testing"""
        self.client = Client()
        
        # Create multiple test records
        for i in range(50):
            Skill.objects.create(
                name=f'Skill {i}',
                category='backend' if i % 2 == 0 else 'frontend',
                proficiency=70 + (i % 30),
                featured=i % 3 == 0
            )
            
            Project.objects.create(
                title=f'Project {i}',
                description=f'Description for project {i}',
                category='web' if i % 3 == 0 else 'ai' if i % 3 == 1 else 'api',
                featured=i % 4 == 0,
                completed_date=date.today() - timedelta(days=i)
            )
    
    def test_home_page_performance(self):
        """Test home page load performance with multiple records"""
        import time
        
        start_time = time.time()
        response = self.client.get(reverse('index'))
        load_time = time.time() - start_time
        
        self.assertEqual(response.status_code, 200)
        self.assertLess(load_time, 1.0)  # Should load in under 1 second
    
    def test_projects_page_performance(self):
        """Test projects page load performance with multiple records"""
        import time
        
        start_time = time.time()
        response = self.client.get(reverse('projects'))
        load_time = time.time() - start_time
        
        self.assertEqual(response.status_code, 200)
        self.assertLess(load_time, 1.0)  # Should load in under 1 second
    
    def test_api_endpoints_performance(self):
        """Test API endpoints performance"""
        import time
        
        # Test skills API
        start_time = time.time()
        response = self.client.get(reverse('api_skills'))
        skills_load_time = time.time() - start_time
        
        self.assertEqual(response.status_code, 200)
        self.assertLess(skills_load_time, 0.5)  # Should load in under 0.5 seconds
        
        # Test projects API
        start_time = time.time()
        response = self.client.get(reverse('api_projects'))
        projects_load_time = time.time() - start_time
        
        self.assertEqual(response.status_code, 200)
        self.assertLess(projects_load_time, 0.5)  # Should load in under 0.5 seconds

