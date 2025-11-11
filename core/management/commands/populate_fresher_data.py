from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Skill, Project, Experience, Education, Certification
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with fresher portfolio data for a final year student'

    def handle(self, *args, **options):
        self.stdout.write('Creating fresher portfolio data...')

        # Create a user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='siddharth',
            defaults={
                'first_name': 'Siddharth',
                'last_name': 'Mishra',
                'email': 'siddharthmishr125@gmail.com',
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            self.stdout.write('Created user: siddharth')

        # Create profile for a final year student
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'title': 'Python Developer — Full-Stack & AI',
                'bio': 'Passionate Python Developer with expertise in Full-Stack Development and Artificial Intelligence. Currently pursuing B.Tech in Computer Science and Engineering (AI) with a strong foundation in modern web technologies and machine learning. Eager to apply my skills in real-world projects and contribute to innovative solutions.',
                'location': 'Greater Noida, Uttar Pradesh',
                'phone': '+91 9936057425',
                'github_url': 'https://github.com/siddharth-mishra',
                'linkedin_url': 'https://linkedin.com/in/siddharth-mishra',
                'twitter_url': 'https://twitter.com/siddharth_mishra',
                'available_for_work': True,
            }
        )
        if created:
            self.stdout.write('Created profile')

        # Create skills appropriate for a final year student
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'featured': True, 'order': 1},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-js-square', 'featured': True, 'order': 2},
            {'name': 'Java', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-java', 'featured': True, 'order': 3},
            {'name': 'C++', 'category': 'backend', 'proficiency': 70, 'icon': 'fas fa-code', 'featured': False, 'order': 4},
            
            # Web Technologies
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-html5', 'featured': True, 'order': 5},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-css3-alt', 'featured': True, 'order': 6},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75, 'icon': 'fab fa-react', 'featured': True, 'order': 7},
            {'name': 'Bootstrap', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-bootstrap', 'featured': False, 'order': 8},
            
            # Backend & Frameworks
            {'name': 'Django', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-python', 'featured': True, 'order': 9},
            {'name': 'Flask', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-python', 'featured': False, 'order': 10},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 70, 'icon': 'fab fa-node-js', 'featured': False, 'order': 11},
            
            # Database
            {'name': 'MySQL', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database', 'featured': True, 'order': 12},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database', 'featured': False, 'order': 13},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 70, 'icon': 'fas fa-database', 'featured': False, 'order': 14},
            
            # AI/ML
            {'name': 'TensorFlow', 'category': 'other', 'proficiency': 75, 'icon': 'fas fa-brain', 'featured': True, 'order': 15},
            {'name': 'Scikit-learn', 'category': 'other', 'proficiency': 80, 'icon': 'fas fa-brain', 'featured': True, 'order': 16},
            {'name': 'OpenCV', 'category': 'other', 'proficiency': 70, 'icon': 'fas fa-eye', 'featured': False, 'order': 17},
            
            # Tools & DevOps
            {'name': 'Git', 'category': 'tools', 'proficiency': 85, 'icon': 'fab fa-git-alt', 'featured': True, 'order': 18},
            {'name': 'GitHub', 'category': 'tools', 'proficiency': 90, 'icon': 'fab fa-github', 'featured': False, 'order': 19},
            {'name': 'VS Code', 'category': 'tools', 'proficiency': 90, 'icon': 'fas fa-code', 'featured': False, 'order': 20},
            {'name': 'Postman', 'category': 'tools', 'proficiency': 80, 'icon': 'fas fa-paper-plane', 'featured': False, 'order': 21},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create projects appropriate for a final year student
        projects_data = [
            {
                'title': 'AI-Powered Resume Parser',
                'description': 'Developed an intelligent resume parsing system using Python, NLP, and machine learning. The system extracts key information from resumes, categorizes skills, and provides insights for HR professionals. Features include PDF parsing, skill extraction, and candidate matching algorithms.',
                'category': 'ai',
                'github_url': 'https://github.com/siddharth-mishra/resume-parser-ai',
                'live_url': 'https://resume-parser-demo.vercel.app',
                'featured': True,
                'completed_date': date.today() - timedelta(days=45),
                'order': 1,
            },
            {
                'title': 'E-Learning Platform',
                'description': 'Built a comprehensive e-learning platform using Django and React. Features include user authentication, course management, video streaming, progress tracking, and interactive quizzes. Implemented real-time notifications and a responsive design for mobile compatibility.',
                'category': 'web',
                'github_url': 'https://github.com/siddharth-mishra/elearning-platform',
                'live_url': 'https://elearning-demo.herokuapp.com',
                'featured': True,
                'completed_date': date.today() - timedelta(days=90),
                'order': 2,
            },
            {
                'title': 'Smart Attendance System',
                'description': 'Created an AI-powered attendance system using facial recognition and computer vision. Built with Python, OpenCV, and Django. Features include real-time face detection, attendance tracking, and automated reporting. Integrated with a web dashboard for administrators.',
                'category': 'ai',
                'github_url': 'https://github.com/siddharth-mishra/smart-attendance',
                'live_url': 'https://attendance-system.vercel.app',
                'featured': True,
                'completed_date': date.today() - timedelta(days=120),
                'order': 3,
            },
            {
                'title': 'Weather Forecast API',
                'description': 'Developed a RESTful weather API using Django REST Framework. Integrates with multiple weather services, provides historical data analysis, and includes caching for performance optimization. Features comprehensive API documentation and rate limiting.',
                'category': 'api',
                'github_url': 'https://github.com/siddharth-mishra/weather-api',
                'live_url': 'https://weather-api-docs.herokuapp.com',
                'featured': False,
                'completed_date': date.today() - timedelta(days=150),
                'order': 4,
            },
            {
                'title': 'Task Management App',
                'description': 'Built a full-stack task management application with React frontend and Django backend. Features include user authentication, task creation/editing, priority levels, due dates, and team collaboration. Implemented real-time updates using WebSockets.',
                'category': 'web',
                'github_url': 'https://github.com/siddharth-mishra/task-manager',
                'live_url': 'https://task-manager-demo.vercel.app',
                'featured': False,
                'completed_date': date.today() - timedelta(days=180),
                'order': 5,
            },
            {
                'title': 'Data Visualization Dashboard',
                'description': 'Created an interactive data visualization dashboard using React and D3.js. Features include multiple chart types, real-time data updates, filtering capabilities, and export functionality. Integrated with various data sources and APIs.',
                'category': 'web',
                'github_url': 'https://github.com/siddharth-mishra/data-viz-dashboard',
                'live_url': 'https://data-viz-demo.vercel.app',
                'featured': False,
                'completed_date': date.today() - timedelta(days=210),
                'order': 6,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add relevant skills to each project
                if project.title == 'AI-Powered Resume Parser':
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='TensorFlow'))
                    project.technologies.add(Skill.objects.get(name='Django'))
                elif project.title == 'E-Learning Platform':
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='MySQL'))
                elif project.title == 'Smart Attendance System':
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='OpenCV'))
                    project.technologies.add(Skill.objects.get(name='Django'))
                elif project.title == 'Weather Forecast API':
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='MySQL'))
                elif project.title == 'Task Management App':
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='JavaScript'))
                elif project.title == 'Data Visualization Dashboard':
                    project.technologies.add(Skill.objects.get(name='React'))
                    project.technologies.add(Skill.objects.get(name='JavaScript'))
                    project.technologies.add(Skill.objects.get(name='Node.js'))
                
                self.stdout.write(f'Created project: {project.title}')

        # Create education (no work experience for fresher)
        education_data = [
            {
                'institution': 'Noida Institute of Engineering and Technology',
                'degree': 'Bachelor of Technology',
                'field_of_study': 'Computer Science and Engineering (AI)',
                'start_date': date(2020, 8, 1),
                'end_date': date(2024, 6, 30),
                'current': True,
                'description': 'Specialized in Artificial Intelligence and Machine Learning. Maintained a strong academic record while actively participating in coding competitions and hackathons. Completed coursework in Data Structures, Algorithms, Database Management, Web Development, and AI/ML.',
            },
            {
                'institution': 'Delhi Public School, Greater Noida',
                'degree': 'Higher Secondary Education',
                'field_of_study': 'Science (PCM)',
                'start_date': date(2018, 4, 1),
                'end_date': date(2020, 3, 31),
                'current': False,
                'description': 'Completed 12th standard with distinction in Science stream. Active participant in science exhibitions and coding clubs.',
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

        # Create certifications relevant for a fresher
        certifications_data = [
            {
                'name': 'Python Programming Certification',
                'issuing_organization': 'Coursera',
                'issue_date': date.today() - timedelta(days=180),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/python-cert',
            },
            {
                'name': 'Machine Learning Specialization',
                'issuing_organization': 'Stanford University (Coursera)',
                'issue_date': date.today() - timedelta(days=120),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/ml-specialization',
            },
            {
                'name': 'Web Development Bootcamp',
                'issuing_organization': 'Udemy',
                'issue_date': date.today() - timedelta(days=90),
                'expiry_date': None,
                'credential_url': 'https://udemy.com/certificate/web-dev',
            },
            {
                'name': 'Django for Beginners',
                'issuing_organization': 'Real Python',
                'issue_date': date.today() - timedelta(days=60),
                'expiry_date': None,
                'credential_url': 'https://realpython.com/certificate/django',
            },
            {
                'name': 'React Fundamentals',
                'issuing_organization': 'Meta (Coursera)',
                'issue_date': date.today() - timedelta(days=45),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/react-fundamentals',
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
            self.style.SUCCESS('Successfully created fresher portfolio data!')
        )
        self.stdout.write('You can now visit http://127.0.0.1:8000 to see your portfolio.')
        self.stdout.write('Admin credentials: username=siddharth, password=password123')

