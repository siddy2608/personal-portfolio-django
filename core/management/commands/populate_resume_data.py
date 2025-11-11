from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth.models import User
from core.models import Profile, Skill, Project, Experience, Education, Certification, Contact

class Command(BaseCommand):
    help = 'Populate database with Siddharth Mishra\'s actual resume data'

    def handle(self, *args, **options):
        self.stdout.write('Creating Siddharth Mishra\'s portfolio data...')
        
        # Clear existing data (except User and Contact)
        self.stdout.write('Clearing existing portfolio data...')
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Profile.objects.all().delete()

        # Create User and Profile
        user, created = User.objects.get_or_create(
            username='siddharth',
            defaults={
                'first_name': 'Siddharth',
                'last_name': 'Mishra',
                'email': 'siddharthmishr125@gmail.com',
            }
        )

        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'title': 'Python Developer — Full-Stack & AI',
                'bio': 'Passionate Python Developer with expertise in Full-Stack Development and Artificial Intelligence. Fresh graduate with B.Tech in Computer Science and Engineering (AI) and a strong foundation in modern web technologies and machine learning. Seeking opportunities to apply my skills and grow professionally.',
                'location': 'Greater Noida, Uttar Pradesh',
                'phone': '+91 9936057425',
                'linkedin_url': 'https://linkedin.com/in/siddharth-mishra',
                'github_url': 'https://github.com/siddharth-mishra',
                'available_for_work': True,
            }
        )

        # Create Skills
        skills_data = [
            # Languages
            {'name': 'Python', 'category': 'backend', 'proficiency': 90, 'icon': 'fab fa-python'},
            {'name': 'Java', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-java'},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-js-square'},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-css3-alt'},
            {'name': 'SQL', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database'},
            
            # Frameworks & Libraries
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python'},
            {'name': 'Flask', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-python'},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75, 'icon': 'fab fa-react'},
            {'name': 'TensorFlow', 'category': 'other', 'proficiency': 70, 'icon': 'fas fa-brain'},
            {'name': 'PyTorch', 'category': 'other', 'proficiency': 65, 'icon': 'fas fa-brain'},
            {'name': 'Scikit-Learn', 'category': 'other', 'proficiency': 80, 'icon': 'fas fa-chart-line'},
            {'name': 'Pandas', 'category': 'other', 'proficiency': 85, 'icon': 'fas fa-table'},
            {'name': 'NumPy', 'category': 'other', 'proficiency': 80, 'icon': 'fas fa-calculator'},
            {'name': 'OpenCV', 'category': 'other', 'proficiency': 75, 'icon': 'fas fa-eye'},
            {'name': 'Matplotlib', 'category': 'other', 'proficiency': 70, 'icon': 'fas fa-chart-bar'},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 70, 'icon': 'fas fa-database'},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 65, 'icon': 'fas fa-database'},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database'},
            {'name': 'Redis', 'category': 'database', 'proficiency': 60, 'icon': 'fas fa-database'},
            
            # Developer Tools
            {'name': 'Git', 'category': 'tools', 'proficiency': 85, 'icon': 'fab fa-git-alt'},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 65, 'icon': 'fab fa-docker'},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 60, 'icon': 'fab fa-aws'},
            {'name': 'Postman', 'category': 'tools', 'proficiency': 80, 'icon': 'fas fa-paper-plane'},
            {'name': 'Jira', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-jira'},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'category': skill_data['category'],
                    'proficiency': skill_data['proficiency'],
                    'icon': skill_data['icon'],
                    'featured': True,
                }
            )

        # No experience - Fresh graduate

        # Create Projects
        projects_data = [
            {
                'title': 'Threat Intelligence Platform (Phishing Detection)',
                'description': 'Spearheaded the development and deployment of a scalable full-stack application on Vercel, providing real-time URL classification to enhance web security for end-users. Trained and fine-tuned Machine Learning models (Logistic Regression, Random Forest) with Scikit-learn, achieving a 95% detection accuracy on a dataset of over 10,000 URLs. Built a secure, high-throughput RESTful API to process asynchronous URL analysis requests and deliver ML-driven threat classifications with sub-second response times.',
                'category': 'ai',
                'github_url': '',
                'live_url': '',
                'featured': True,
                'completed_date': date(2025, 6, 1),
            },
            {
                'title': 'IsharaX (Gesture Control System)',
                'description': 'Created a real-time Human-Computer Interaction (HCI) system using OpenCV and MediaPipe to translate hand gestures into system commands with over 90% recognition accuracy. Integrated the Speech Recognition library to develop a multi-modal command engine, achieving a 95% command success rate for synchronized voice and gesture-based system control.',
                'category': 'ai',
                'github_url': '',
                'live_url': '',
                'featured': True,
                'completed_date': date(2024, 7, 1),
            },
            {
                'title': 'RasoiRack (Recipe Management System)',
                'description': 'Implemented a secure authentication module with role-based access controls (RBAC), managing permissions for 3 distinct user roles. Architected a normalized SQLite database and its corresponding CRUD API, ensuring 100% data integrity across relational tables and providing support for image file uploads.',
                'category': 'web',
                'github_url': '',
                'live_url': '',
                'featured': False,
                'completed_date': date(2022, 1, 1),
            }
        ]

        for proj_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )

        # Create Education
        education_data = [
            {
                'institution': 'Noida Institute of Engineering and Technology',
                'degree': 'B.Tech - Computer Science and Engineering (AI)',
                'field_of_study': 'Computer Science and Engineering (AI)',
                'start_date': date(2022, 1, 1),
                'end_date': date(2026, 12, 31),
                'current': True,
                'description': 'CGPA: 7.50 | Greater Noida, Uttar Pradesh',
            },
            {
                'institution': 'Udaya Public School',
                'degree': 'CBSE 12th',
                'field_of_study': 'Science',
                'start_date': date(2020, 1, 1),
                'end_date': date(2021, 12, 31),
                'current': False,
                'description': 'Percentage: 80% | Ayodhya, U.P',
            },
            {
                'institution': 'D.R.M Public School',
                'degree': 'CBSE 10th',
                'field_of_study': 'General',
                'start_date': date(2017, 1, 1),
                'end_date': date(2018, 12, 31),
                'current': False,
                'description': 'Percentage: 90% | Ayodhya, U.P',
            }
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )

        # Create Certifications
        certifications_data = [
            {
                'name': 'Python for Data Science, AI & Development',
                'issuing_organization': 'Coursera',
                'issue_date': date.today() - timedelta(days=180),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/python-data-science',
            },
            {
                'name': 'Building AI Powered Chatbots Without Programming',
                'issuing_organization': 'Coursera',
                'issue_date': date.today() - timedelta(days=150),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/ai-chatbots',
            },
            {
                'name': 'ReactJS',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date.today() - timedelta(days=120),
                'expiry_date': None,
                'credential_url': 'https://springboard.infosys.com/certificates/reactjs',
            },
            {
                'name': 'Deep Learning for Developers',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date.today() - timedelta(days=90),
                'expiry_date': None,
                'credential_url': 'https://springboard.infosys.com/certificates/deep-learning',
            },
            {
                'name': 'Java Programming Fundamentals',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date.today() - timedelta(days=60),
                'expiry_date': None,
                'credential_url': 'https://springboard.infosys.com/certificates/java',
            },
            {
                'name': 'Introduction to Artificial Intelligence (AI)',
                'issuing_organization': 'Coursera',
                'issue_date': date.today() - timedelta(days=30),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/intro-ai',
            }
        ]

        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuing_organization=cert_data['issuing_organization'],
                defaults=cert_data
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created Siddharth Mishra\'s portfolio data!')
        )
        self.stdout.write('You can now visit http://127.0.0.1:8000 to see your portfolio.')
