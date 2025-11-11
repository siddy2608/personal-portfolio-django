from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Skill, Project, Experience, Education, Certification
from datetime import date


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Create superuser
        user, created = User.objects.get_or_create(
            username='siddharth',
            defaults={
                'email': 'siddharthmishr125@gmail.com',
                'first_name': 'Siddharth',
                'last_name': 'Mishra',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser'))

        # Create Profile
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'title': 'Python Developer & AI Engineer',
                'bio': 'I am a passionate Python developer and AI engineer with expertise in building scalable web applications and intelligent systems. I love solving complex problems and creating innovative solutions.',
                'location': 'Greater Noida, India',
                'phone': '+91 9936057425',
                'github_url': 'https://github.com/siddharthmishr125',
                'linkedin_url': 'https://www.linkedin.com/in/siddharth-mishra-dev/',
                'available_for_work': True,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile'))

        # Create Skills
        skills_data = [
            # Backend
            {'name': 'Python', 'category': 'backend', 'proficiency': 90, 'icon': 'fab fa-python', 'featured': True},
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'featured': True},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-node-js', 'featured': True},
            {'name': 'Express.js', 'category': 'backend', 'proficiency': 70, 'icon': 'fab fa-node-js'},
            
            # Frontend
            {'name': 'React', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-react', 'featured': True},
            {'name': 'Angular', 'category': 'frontend', 'proficiency': 75, 'icon': 'fab fa-angular', 'featured': True},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-css3-alt'},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-js', 'featured': True},
            
            # Database
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database', 'featured': True},
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database'},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 70, 'icon': 'fas fa-database'},
            
            # Tools
            {'name': 'Git', 'category': 'tools', 'proficiency': 85, 'icon': 'fab fa-git-alt', 'featured': True},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-docker'},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 65, 'icon': 'fab fa-aws'},
        ]

        for i, skill_data in enumerate(skills_data):
            skill_data['order'] = i
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))

        # Create Projects
        projects_data = [
            {
                'title': 'Student Management System',
                'description': 'A comprehensive student management system with features for attendance tracking, grade management, and parent communication.',
                'category': 'web',
                'github_url': 'https://github.com/yourusername/student-management',
                'featured': True,
                'completed_date': date(2024, 3, 15),
            },
            {
                'title': 'AI Tutor Platform',
                'description': 'An AI-powered tutoring platform that provides personalized learning experiences using machine learning algorithms.',
                'category': 'ai',
                'github_url': 'https://github.com/yourusername/ai-tutor',
                'featured': True,
                'completed_date': date(2024, 6, 20),
            },
            {
                'title': 'E-commerce API',
                'description': 'RESTful API for an e-commerce platform with features like product management, order processing, and payment integration.',
                'category': 'api',
                'github_url': 'https://github.com/yourusername/ecommerce-api',
                'featured': False,
                'completed_date': date(2024, 1, 10),
            },
        ]

        for i, project_data in enumerate(projects_data):
            project_data['order'] = i
            # Pop technologies to handle many-to-many separately
            techs = project_data.pop('technologies', [])
            
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            
            if created:
                # Add some technologies
                if i == 0:  # Student Management System
                    project.technologies.add(
                        Skill.objects.get(name='Python'),
                        Skill.objects.get(name='Django'),
                        Skill.objects.get(name='React'),
                        Skill.objects.get(name='PostgreSQL'),
                    )
                elif i == 1:  # AI Tutor
                    project.technologies.add(
                        Skill.objects.get(name='Python'),
                        Skill.objects.get(name='React'),
                        Skill.objects.get(name='MongoDB'),
                    )
                elif i == 2:  # E-commerce API
                    project.technologies.add(
                        Skill.objects.get(name='Node.js'),
                        Skill.objects.get(name='Express.js'),
                        Skill.objects.get(name='MongoDB'),
                    )
                
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))

        # Create Experience
        experience_data = {
            'company': 'Codesoft',
            'position': 'Web Developer Intern',
            'description': 'Developed and maintained web applications using modern technologies. Collaborated with team members on various projects.',
            'start_date': date(2025, 1, 1),
            'current': True,
            'location': 'Remote',
        }

        experience, created = Experience.objects.get_or_create(
            company=experience_data['company'],
            position=experience_data['position'],
            defaults=experience_data
        )
        
        if created:
            experience.technologies.add(
                Skill.objects.get(name='Python'),
                Skill.objects.get(name='Django'),
                Skill.objects.get(name='React'),
            )
            self.stdout.write(self.style.SUCCESS('Created experience'))

        # Create Education
        education_data = {
            'institution': 'Noida Institute of Engineering and Technology',
            'degree': 'B.Tech',
            'field_of_study': 'Computer Science Engineering (AI)',
            'start_date': date(2022, 8, 1),
            'end_date': date(2026, 6, 30),
            'current': True,
            'description': 'Specializing in Artificial Intelligence with focus on machine learning and data science.',
        }

        education, created = Education.objects.get_or_create(
            institution=education_data['institution'],
            degree=education_data['degree'],
            defaults=education_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created education'))

        # Create Certifications
        certifications_data = [
            {
                'name': 'Certified in Cybersecurity',
                'issuing_organization': 'ISC2',
                'issue_date': date(2024, 7, 1),
                'credential_id': 'CC-123456',
            },
            {
                'name': 'Python for Data Science',
                'issuing_organization': 'IBM',
                'issue_date': date(2024, 8, 1),
                'credential_id': 'PDS-789012',
            },
        ]

        for cert_data in certifications_data:
            cert, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created certification: {cert.name}'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
