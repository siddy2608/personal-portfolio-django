from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Contact
import re


class ContactForm(forms.ModelForm):
    """Contact form with validation and security measures"""
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'maxlength': '100',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'maxlength': '200',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message...',
                'rows': '5',
                'maxlength': '2000',
            }),
        }
    
    def clean_name(self):
        """Validate name field"""
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Name is required.')
        
        # Remove extra whitespace
        name = ' '.join(name.split())
        
        # Check for minimum length
        if len(name) < 2:
            raise ValidationError('Name must be at least 2 characters long.')
        
        # Check for valid characters (letters, spaces, hyphens, apostrophes)
        if not re.match(r'^[a-zA-Z\s\-\']+$', name):
            raise ValidationError('Name can only contain letters, spaces, hyphens, and apostrophes.')
        
        return name
    
    def clean_email(self):
        """Validate email field"""
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required.')
        
        # Use Django's built-in email validator
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError:
            raise ValidationError('Please enter a valid email address.')
        
        # Check for disposable email domains (basic check)
        disposable_domains = [
            '10minutemail.com', 'guerrillamail.com', 'tempmail.org',
            'mailinator.com', 'throwaway.email', 'temp-mail.org'
        ]
        domain = email.split('@')[1].lower()
        if domain in disposable_domains:
            raise ValidationError('Please use a valid email address.')
        
        return email.lower()
    
    def clean_subject(self):
        """Validate subject field"""
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise ValidationError('Subject is required.')
        
        # Remove extra whitespace
        subject = ' '.join(subject.split())
        
        # Check for minimum length
        if len(subject) < 5:
            raise ValidationError('Subject must be at least 5 characters long.')
        
        # Check for maximum length
        if len(subject) > 200:
            raise ValidationError('Subject cannot exceed 200 characters.')
        
        return subject
    
    def clean_message(self):
        """Validate message field"""
        message = self.cleaned_data.get('message')
        if not message:
            raise ValidationError('Message is required.')
        
        # Remove extra whitespace
        message = ' '.join(message.split())
        
        # Check for minimum length
        if len(message) < 10:
            raise ValidationError('Message must be at least 10 characters long.')
        
        # Check for maximum length
        if len(message) > 2000:
            raise ValidationError('Message cannot exceed 2000 characters.')
        
        # Basic spam detection
        spam_indicators = [
            'buy now', 'click here', 'free money', 'lottery winner',
            'urgent reply', 'limited time', 'act now', 'make money fast'
        ]
        message_lower = message.lower()
        spam_count = sum(1 for indicator in spam_indicators if indicator in message_lower)
        
        if spam_count >= 2:
            raise ValidationError('Your message appears to be spam. Please write a genuine message.')
        
        return message
    
    def clean(self):
        """Additional form-level validation"""
        cleaned_data = super().clean()
        
        # Check for rapid submissions (basic rate limiting)
        # This is a simple check - in production, use proper rate limiting middleware
        
        return cleaned_data


class FileUploadForm(forms.Form):
    """Form for secure file uploads"""
    
    def __init__(self, *args, **kwargs):
        self.allowed_types = kwargs.pop('allowed_types', [])
        self.max_size = kwargs.pop('max_size', 5 * 1024 * 1024)  # 5MB default
        super().__init__(*args, **kwargs)
    
    file = forms.FileField(
        label='Select File',
        help_text=f'Maximum file size: {self.max_size // (1024*1024)}MB'
    )
    
    def clean_file(self):
        """Validate uploaded file"""
        uploaded_file = self.cleaned_data.get('file')
        
        if not uploaded_file:
            raise ValidationError('Please select a file to upload.')
        
        # Check file size
        if uploaded_file.size > self.max_size:
            raise ValidationError(f'File size must be under {self.max_size // (1024*1024)}MB.')
        
        # Check file type
        if self.allowed_types and uploaded_file.content_type not in self.allowed_types:
            raise ValidationError(f'File type not allowed. Allowed types: {", ".join(self.allowed_types)}')
        
        # Check file extension
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx']
        file_extension = uploaded_file.name.lower()
        if not any(file_extension.endswith(ext) for ext in allowed_extensions):
            raise ValidationError('File extension not allowed.')
        
        return uploaded_file

