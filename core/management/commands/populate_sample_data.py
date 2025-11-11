from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Skill, Project, Experience, Education, Certification
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample portfolio data...')

        # Create a user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='siddharth',
            defaults={
                'first_name': 'Siddharth',
                'last_name': 'Mishra',
                'email': 'siddharth@example.com',
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            self.stdout.write('Created user: siddharth')

        # Create profile
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'title': 'Full Stack Developer',
                'bio': 'Passionate Full Stack Developer with expertise in modern web technologies. I love creating innovative solutions that make a difference in people\'s lives. With a strong foundation in both frontend and backend development, I bring ideas to life through clean, efficient, and scalable code.',
                'location': 'New York, NY',
                'phone': '+1 (555) 123-4567',
                'github_url': 'https://github.com/siddharth',
                'linkedin_url': 'https://linkedin.com/in/siddharth',
                'twitter_url': 'https://twitter.com/siddharth',
                'available_for_work': True,
            }
        )
        if created:
            self.stdout.write('Created profile')

        # Create skills
        skills_data = [
            # Frontend
            {'name': 'React', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-react', 'featured': True, 'order': 1},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 95, 'icon': 'fab fa-js-square', 'featured': True, 'order': 2},
            {'name': 'TypeScript', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-js-square', 'featured': True, 'order': 3},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 95, 'icon': 'fab fa-html5', 'featured': False, 'order': 4},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-css3-alt', 'featured': False, 'order': 5},
            {'name': 'Bootstrap', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-bootstrap', 'featured': False, 'order': 6},
            
            # Backend
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'featured': True, 'order': 7},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-node-js', 'featured': True, 'order': 8},
            {'name': 'Python', 'category': 'backend', 'proficiency': 90, 'icon': 'fab fa-python', 'featured': False, 'order': 9},
            {'name': 'Express.js', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-node-js', 'featured': False, 'order': 10},
            
            # Database
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database', 'featured': True, 'order': 11},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database', 'featured': False, 'order': 12},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database', 'featured': False, 'order': 13},
            
            # Tools & DevOps
            {'name': 'Git', 'category': 'tools', 'proficiency': 90, 'icon': 'fab fa-git-alt', 'featured': True, 'order': 14},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-docker', 'featured': False, 'order': 15},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 65, 'icon': 'fab fa-aws', 'featured': False, 'order': 16},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-stack e-commerce solution built with React frontend and Django backend. Features include user authentication, payment processing with Stripe, inventory management, and admin dashboard. The platform supports multiple payment methods and provides real-time order tracking.',
                'category': 'web',
                'github_url': 'https://github.com/siddharth/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.example.com',
                'featured': True,
                'completed_date': date.today() - timedelta(days=30),
                'order': 1,
            },
            {
                'title': 'Task Management App',
                'description': 'Cross-platform task management application with offline sync capabilities. Built with React Native for mobile and React for web. Features include team collaboration, real-time notifications, file sharing, and progress tracking with analytics.',
                'category': 'mobile',
                'github_url': 'https://github.com/siddharth/task-manager',
                'live_url': 'https://taskmanager.example.com',
                'featured': True,
                'completed_date': date.today() - timedelta(days=60),
                'order': 2,
            },
            {
                'title': 'Analytics Dashboard',
                'description': 'Real-time analytics dashboard with interactive charts and data visualization. Built with React and D3.js for frontend, Node.js backend with Socket.io for real-time updates. Features customizable widgets and export capabilities.',
                'category': 'web',
                'github_url': 'https://github.com/siddharth/analytics-dashboard',
                'live_url': 'https://analytics.example.com',
                'featured': True,
                'completed_date': date.today() - timedelta(days=90),
                'order': 3,
            },
            {
                'title': 'AI Chat Assistant',
                'description': 'Intelligent chatbot powered by machine learning algorithms. Built with Python, TensorFlow, and React. Features natural language processing, sentiment analysis, and integration with multiple messaging platforms.',
                'category': 'ai',
                'github_url': 'https://github.com/siddharth/ai-chatbot',
                'live_url': 'https://chatbot.example.com',
                'featured': False,
                'completed_date': date.today() - timedelta(days=120),
                'order': 4,
            },
            {
                'title': 'REST API Service',
                'description': 'Comprehensive REST API service for a social media platform. Built with Django REST Framework, featuring JWT authentication, rate limiting, caching with Redis, and comprehensive API documentation with Swagger.',
                'category': 'api',
                'github_url': 'https://github.com/siddharth/social-api',
                'live_url': 'https://api.example.com/docs',
                'featured': False,
                'completed_date': date.today() - timedelta(days=150),
                'order': 5,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add some skills to the project
                if project.title == 'E-Commerce Platform':
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='PostgreSQL'))
                elif project.title == 'Task Management App':
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='Node.js'))
                    project.technologies.add(Skill.objects.get(name='MongoDB'))
                elif project.title == 'Analytics Dashboard':
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='Node.js'))
                    project.technologies.add(Skill.objects.get(name='JavaScript'))
                elif project.title == 'AI Chat Assistant':
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='React'))
                elif project.title == 'REST API Service':
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='PostgreSQL'))
                
                self.stdout.write(f'Created project: {project.title}')

        # Create experience
        experiences_data = [
            {
                'company': 'TechCorp Solutions',
                'position': 'Senior Full Stack Developer',
                'description': 'Led development of multiple web applications using React, Node.js, and Django. Mentored junior developers and implemented best practices for code quality and deployment. Collaborated with cross-functional teams to deliver high-quality software solutions.',
                'start_date': date.today() - timedelta(days=365*2),
                'end_date': None,
                'current': True,
                'location': 'New York, NY',
            },
            {
                'company': 'StartupXYZ',
                'position': 'Frontend Developer',
                'description': 'Developed responsive web applications using React and TypeScript. Worked closely with designers to implement pixel-perfect UI components. Optimized application performance and improved user experience.',
                'start_date': date.today() - timedelta(days=365*3),
                'end_date': date.today() - timedelta(days=365*2),
                'current': False,
                'location': 'San Francisco, CA',
            },
            {
                'company': 'Digital Innovations',
                'position': 'Junior Developer',
                'description': 'Built and maintained web applications using Django and Python. Participated in code reviews and contributed to team documentation. Learned modern development practices and tools.',
                'start_date': date.today() - timedelta(days=365*4),
                'end_date': date.today() - timedelta(days=365*3),
                'current': False,
                'location': 'Boston, MA',
            },
        ]

        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience.position} at {experience.company}')

        # Create education
        education_data = [
            {
                'institution': 'Massachusetts Institute of Technology',
                'degree': 'Master of Science',
                'field_of_study': 'Computer Science',
                'start_date': date.today() - timedelta(days=365*6),
                'end_date': date.today() - timedelta(days=365*4),
            },
            {
                'institution': 'Stanford University',
                'degree': 'Bachelor of Science',
                'field_of_study': 'Computer Engineering',
                'start_date': date.today() - timedelta(days=365*8),
                'end_date': date.today() - timedelta(days=365*6),
            },
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                field_of_study=edu_data['field_of_study'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education.degree} in {education.field_of_study}')

        # Create certifications
        certifications_data = [
            {
                'name': 'AWS Certified Solutions Architect',
                'issuing_organization': 'Amazon Web Services',
                'issue_date': date.today() - timedelta(days=180),
                'expiry_date': date.today() + timedelta(days=365*2),
                'credential_url': 'https://aws.amazon.com/certification/',
            },
            {
                'name': 'Google Cloud Professional Developer',
                'issuing_organization': 'Google',
                'issue_date': date.today() - timedelta(days=365),
                'expiry_date': date.today() + timedelta(days=365*2),
                'credential_url': 'https://cloud.google.com/certification/',
            },
            {
                'name': 'Microsoft Certified: Azure Developer Associate',
                'issuing_organization': 'Microsoft',
                'issue_date': date.today() - timedelta(days=90),
                'expiry_date': date.today() + timedelta(days=365*2),
                'credential_url': 'https://www.microsoft.com/certification/',
            },
        ]

        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuing_organization=cert_data['issuing_organization'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certification: {certification.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample portfolio data!')
        )
        self.stdout.write('You can now visit http://127.0.0.1:8000 to see your portfolio.')
        self.stdout.write('Admin credentials: username=admin, password=password123')
