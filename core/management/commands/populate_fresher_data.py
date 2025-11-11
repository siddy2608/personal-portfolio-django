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

        # Create skills matching resume
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'featured': True, 'order': 1},
            {'name': 'Java', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-java', 'featured': True, 'order': 2},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-js-square', 'featured': True, 'order': 3},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-html5', 'featured': True, 'order': 4},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 88, 'icon': 'fab fa-css3-alt', 'featured': True, 'order': 5},
            {'name': 'SQL', 'category': 'database', 'proficiency': 82, 'icon': 'fas fa-database', 'featured': True, 'order': 6},
            
            # Frameworks & Libraries
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'featured': True, 'order': 7},
            {'name': 'Flask', 'category': 'backend', 'proficiency': 78, 'icon': 'fab fa-python', 'featured': True, 'order': 8},
            {'name': 'React', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-react', 'featured': True, 'order': 9},
            {'name': 'TensorFlow', 'category': 'other', 'proficiency': 75, 'icon': 'fas fa-brain', 'featured': True, 'order': 10},
            {'name': 'PyTorch', 'category': 'other', 'proficiency': 72, 'icon': 'fas fa-brain', 'featured': True, 'order': 11},
            {'name': 'Scikit-learn', 'category': 'other', 'proficiency': 82, 'icon': 'fas fa-brain', 'featured': True, 'order': 12},
            {'name': 'Pandas', 'category': 'other', 'proficiency': 80, 'icon': 'fas fa-chart-line', 'featured': False, 'order': 13},
            {'name': 'NumPy', 'category': 'other', 'proficiency': 78, 'icon': 'fas fa-calculator', 'featured': False, 'order': 14},
            {'name': 'OpenCV', 'category': 'other', 'proficiency': 80, 'icon': 'fas fa-eye', 'featured': True, 'order': 15},
            {'name': 'Matplotlib', 'category': 'other', 'proficiency': 75, 'icon': 'fas fa-chart-bar', 'featured': False, 'order': 16},
            {'name': 'MediaPipe', 'category': 'other', 'proficiency': 75, 'icon': 'fas fa-hand-paper', 'featured': False, 'order': 17},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database', 'featured': True, 'order': 18},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 82, 'icon': 'fas fa-database', 'featured': True, 'order': 19},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database', 'featured': True, 'order': 20},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database', 'featured': True, 'order': 21},
            {'name': 'Redis', 'category': 'database', 'proficiency': 70, 'icon': 'fas fa-database', 'featured': False, 'order': 22},
            
            # Developer Tools
            {'name': 'Git', 'category': 'tools', 'proficiency': 88, 'icon': 'fab fa-git-alt', 'featured': True, 'order': 23},
            {'name': 'GitHub', 'category': 'tools', 'proficiency': 90, 'icon': 'fab fa-github', 'featured': True, 'order': 24},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 75, 'icon': 'fab fa-docker', 'featured': True, 'order': 25},
            {'name': 'Postman', 'category': 'tools', 'proficiency': 85, 'icon': 'fas fa-paper-plane', 'featured': True, 'order': 26},
            {'name': 'Jira', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-jira', 'featured': False, 'order': 27},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 72, 'icon': 'fab fa-aws', 'featured': True, 'order': 28},
            {'name': 'Vercel', 'category': 'tools', 'proficiency': 80, 'icon': 'fas fa-cloud', 'featured': False, 'order': 29},
            {'name': 'Netlify', 'category': 'tools', 'proficiency': 75, 'icon': 'fas fa-cloud', 'featured': False, 'order': 30},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create projects matching resume
        projects_data = [
            {
                'title': 'Threat Intelligence Platform (Phishing Detection)',
                'description': 'Spearheaded the development and deployment of a scalable full-stack application on Vercel, providing real-time URL classification to enhance web security for end-users. Trained and fine-tuned Machine Learning models (Logistic Regression, Random Forest) with Scikit-learn, achieving a 95% detection accuracy on a dataset of over 10,000 URLs. Built a secure, high-throughput RESTful API to process asynchronous URL analysis requests and deliver ML-driven threat classifications with sub-second response times.',
                'category': 'ai',
                'github_url': 'https://github.com/siddy2608/threat-intelligence-platform',
                'live_url': 'https://threat-intelligence.vercel.app',
                'featured': True,
                'completed_date': date(2025, 6, 15),
                'order': 1,
            },
            {
                'title': 'IsharaX (Gesture Control System)',
                'description': 'Created a real-time Human-Computer Interaction (HCI) system using OpenCV and MediaPipe to translate hand gestures into system commands with over 90% recognition accuracy. Integrated the Speech Recognition library to develop a multi-modal command engine, achieving a 95% command success rate for synchronized voice and gesture-based system control.',
                'category': 'ai',
                'github_url': 'https://github.com/siddy2608/isharax',
                'live_url': 'https://isharax-demo.vercel.app',
                'featured': True,
                'completed_date': date(2024, 7, 20),
                'order': 2,
            },
            {
                'title': 'RasoiRack (Recipe Management System)',
                'description': 'Implemented a secure authentication module with role-based access controls (RBAC), managing permissions for 3 distinct user roles. Architected a normalized SQLite database and its corresponding CRUD API, ensuring 100% data integrity across relational tables and providing support for image file uploads.',
                'category': 'web',
                'github_url': 'https://github.com/siddy2608/rasoirack',
                'live_url': 'https://rasoirack.vercel.app',
                'featured': True,
                'completed_date': date(2022, 1, 15),
                'order': 3,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add relevant skills to each project
                if project.title == 'Threat Intelligence Platform (Phishing Detection)':
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='Scikit-learn'))
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='PostgreSQL'))
                elif project.title == 'IsharaX (Gesture Control System)':
                    project.technologies.add(Skill.objects.get(name='OpenCV'))
                    project.technologies.add(Skill.objects.get(name='Python'))
                    try:
                        project.technologies.add(Skill.objects.get(name='MediaPipe'))
                    except Skill.DoesNotExist:
                        pass
                elif project.title == 'RasoiRack (Recipe Management System)':
                    project.technologies.add(Skill.objects.get(name='Django'))
                    project.technologies.add(Skill.objects.get(name='Python'))
                    project.technologies.add(Skill.objects.get(name='SQLite'))
                
                self.stdout.write(f'Created project: {project.title}')

        # Create experience
        experience_data = [
            {
                'company': 'Codesoft',
                'position': 'Web Developer Intern',
                'description': 'Crafted responsive and interactive UIs with React and modern CSS3, improving user accessibility and engagement across devices. Engineered scalable RESTful APIs with Django Rest Framework, enabling seamless front-end to back-end communication and implementing comprehensive CRUD operations. Utilized Git and GitHub for version control within an Agile/Scrum framework, managing codebase, reviewing pull requests, and resolving merge conflicts. Reduced critical errors by over 20%.',
                'start_date': date(2025, 2, 1),
                'end_date': date(2025, 3, 31),
                'current': False,
                'location': 'Remote',
            },
        ]

        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                start_date=exp_data['start_date'],
                defaults=exp_data
            )
            if created:
                # Add relevant skills to experience
                experience.technologies.add(Skill.objects.get(name='React'))
                experience.technologies.add(Skill.objects.get(name='Django'))
                experience.technologies.add(Skill.objects.get(name='CSS3'))
                experience.technologies.add(Skill.objects.get(name='Git'))
                experience.technologies.add(Skill.objects.get(name='GitHub'))
                self.stdout.write(f'Created experience: {experience.position} at {experience.company}')

        # Create education matching resume
        education_data = [
            {
                'institution': 'Noida Institute of Engineering and Technology',
                'degree': 'B.Tech - Computer Science and Engineering (AI)',
                'field_of_study': 'Computer Science and Engineering (AI)',
                'start_date': date(2022, 8, 1),
                'end_date': date(2026, 6, 30),
                'current': True,
                'description': 'CGPA: 7.50. Specialized in Artificial Intelligence and Machine Learning. Located in Greater Noida, Uttar Pradesh.',
            },
            {
                'institution': 'Udaya Public School',
                'degree': 'CBSE - 12th',
                'field_of_study': 'Science (PCM)',
                'start_date': date(2020, 4, 1),
                'end_date': date(2021, 3, 31),
                'current': False,
                'description': 'Percentage: 80%. Completed 12th standard with distinction in Science stream. Located in Ayodhya, U.P.',
            },
            {
                'institution': 'D.R.M Public School',
                'degree': 'CBSE - 10th',
                'field_of_study': 'General',
                'start_date': date(2017, 4, 1),
                'end_date': date(2018, 3, 31),
                'current': False,
                'description': 'Percentage: 90%. Completed 10th standard with excellent academic performance. Located in Ayodhya, U.P.',
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

        # Create certifications matching resume
        certifications_data = [
            {
                'name': 'Python for Data Science, AI & Development',
                'issuing_organization': 'Coursera',
                'issue_date': date(2024, 6, 1),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/python-data-science',
            },
            {
                'name': 'Building AI Powered Chatbots Without Programming',
                'issuing_organization': 'Coursera',
                'issue_date': date(2024, 8, 1),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/ai-chatbots',
            },
            {
                'name': 'ReactJS',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date(2024, 9, 1),
                'expiry_date': None,
                'credential_url': 'https://infosysspringboard.com/certificate/reactjs',
            },
            {
                'name': 'Deep Learning for Developers',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date(2024, 10, 1),
                'expiry_date': None,
                'credential_url': 'https://infosysspringboard.com/certificate/deep-learning',
            },
            {
                'name': 'Java Programming Fundamentals',
                'issuing_organization': 'Infosys Springboard',
                'issue_date': date(2024, 5, 1),
                'expiry_date': None,
                'credential_url': 'https://infosysspringboard.com/certificate/java',
            },
            {
                'name': 'Introduction to Artificial Intelligence (AI)',
                'issuing_organization': 'Coursera',
                'issue_date': date(2024, 7, 1),
                'expiry_date': None,
                'credential_url': 'https://coursera.org/verify/intro-ai',
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

