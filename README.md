# Siddharth's Portfolio - Django

A modern, professional portfolio website built with Django showcasing skills, projects, and experience.

## 🚀 Features

- **Modern Design**: Clean, professional design with smooth animations
- **Responsive Layout**: Fully responsive across all devices
- **Dynamic Content**: Database-driven content management
- **Contact Form**: Functional contact form with email notifications
- **Project Showcase**: Beautiful project gallery with filtering
- **Skills Display**: Interactive skills section with progress bars
- **Professional Styling**: Custom CSS with modern design system

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS
- **Icons**: Font Awesome 6
- **Fonts**: Inter & JetBrains Mono

## 📁 Project Structure

```
portfolio_django/
├── core/                    # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   └── templates/core/     # HTML templates
├── portfolio_django/        # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── static/                 # Static files (CSS, JS, images)
├── manage.py               # Django management script
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd siddharth-resume
   ```

2. **Create virtual environment**
   ```bash
   python -m venv django_env
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   django_env\Scripts\activate
   
   # macOS/Linux
   source django_env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django djangorestframework django-cors-headers pillow
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the site**
   Open your browser and go to `http://127.0.0.1:8000`

## 📊 Database Models

### Profile
- User information and bio
- Social media links
- Contact details
- Profile image

### Skill
- Skill name and category
- Proficiency level (0-100)
- Icon and featured status
- Ordering

### Project
- Project title and description
- Category and technologies
- GitHub and live URLs
- Featured status and completion date

### Experience
- Company and position
- Description and technologies
- Start/end dates
- Company logo

### Education
- Institution and degree
- Field of study
- Start/end dates

### Certification
- Certification name and issuer
- Issue date and expiry
- Credential URL

### Contact
- Contact form submissions
- Name, email, subject, message
- Status tracking

## 🎨 Design Features

### Color Palette
- **Primary**: Deep Ocean Blue (#0A2342)
- **Accent**: Vibrant Orange (#FF6B35)
- **Secondary**: Teal (#2E8B8B)
- **Background**: Warm White (#FDFBF7)

### Typography
- **Primary Font**: Inter (clean, modern)
- **Code Font**: JetBrains Mono (for code snippets)

### Components
- **Glassmorphism**: Subtle backdrop blur effects
- **Gradients**: Modern gradient backgrounds
- **Shadows**: Layered shadow system
- **Animations**: Smooth hover and scroll animations

## 📱 Pages

### Home (`/`)
- Hero section with introduction
- Skills showcase
- Featured projects
- Call-to-action

### About (`/about/`)
- Detailed bio and experience
- Skills breakdown
- Education and certifications
- Timeline view

### Projects (`/projects/`)
- Project gallery with filtering
- Search functionality
- Category filtering
- Project details

### Contact (`/contact/`)
- Contact form
- Contact information
- Social media links

## 🔧 Customization

### Adding Content

1. **Access Admin Panel**
   - Go to `http://127.0.0.1:8000/admin`
   - Login with superuser credentials

2. **Add Profile Information**
   - Navigate to "Profiles"
   - Add your personal information

3. **Add Skills**
   - Go to "Skills"
   - Add your technical skills with proficiency levels

4. **Add Projects**
   - Navigate to "Projects"
   - Add your portfolio projects with details

5. **Add Experience**
   - Go to "Experiences"
   - Add your work history

### Styling Customization

The design system uses CSS custom properties (variables) for easy customization:

```css
:root {
    --primary-color: #0A2342;    /* Main brand color */
    --accent-color: #FF6B35;     /* Accent color */
    --background-color: #FDFBF7; /* Background color */
    /* ... more variables */
}
```

## 🚀 Deployment

### Production Settings

1. **Update settings.py**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

2. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

3. **Database**
   - Consider using PostgreSQL for production
   - Update DATABASES setting

4. **Environment Variables**
   - Set SECRET_KEY as environment variable
   - Configure email settings

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **Vercel**: Static hosting with Django API
- **Railway**: Modern deployment platform

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

- **Email**: siddharth@example.com
- **LinkedIn**: [Your LinkedIn]
- **GitHub**: [Your GitHub]

---

Built with ❤️ using Django

