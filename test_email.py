#!/usr/bin/env python3
"""
Simple Email Test Script
This script tests if your Gmail configuration is working.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_django.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email_configuration():
    """Test the email configuration"""
    
    print("🧪 Testing Email Configuration")
    print("=" * 40)
    
    # Check if app password is configured
    if settings.EMAIL_HOST_PASSWORD == 'your_16_character_app_password_here':
        print("❌ App password not configured!")
        print("Please update portfolio_django/settings.py with your Gmail app password")
        print("Follow the instructions in EMAIL_SETUP_GUIDE.md")
        return False
    
    print(f"📧 Email Host: {settings.EMAIL_HOST}")
    print(f"📧 Email User: {settings.EMAIL_HOST_USER}")
    print(f"📧 App Password: {'*' * len(settings.EMAIL_HOST_PASSWORD)}")
    
    try:
        # Send a test email
        subject = "Test Email from Portfolio"
        message = "This is a test email to verify your Gmail configuration is working correctly."
        
        print("\n📤 Sending test email...")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        print("✅ Test email sent successfully!")
        print(f"📧 Check your inbox at {settings.EMAIL_HOST_USER}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send test email: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure 2-Factor Authentication is enabled")
        print("2. Make sure you're using the app password (not regular password)")
        print("3. Check that the app password is 16 characters long")
        print("4. Try generating a new app password")
        return False

if __name__ == "__main__":
    test_email_configuration()



