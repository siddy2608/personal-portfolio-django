#!/usr/bin/env python3
"""
Quick Email Setup Script for Siddharth's Portfolio
This script helps you set up Gmail credentials for email notifications.
"""

import os
import re

def update_settings_file():
    """Update the Django settings file with Gmail credentials"""
    
    print("🔐 Gmail Email Setup for Portfolio Notifications")
    print("=" * 50)
    
    # Get Gmail app password from user
    print("\n📧 To enable email notifications, you need to:")
    print("1. Enable 2-Factor Authentication on your Gmail account")
    print("2. Generate an App Password for 'Mail'")
    print("3. Enter the 16-character app password below")
    
    while True:
        app_password = input("\n🔑 Enter your Gmail App Password (16 characters): ").strip()
        
        if len(app_password) == 16 and app_password.isalnum():
            break
        else:
            print("❌ Invalid app password. It should be exactly 16 alphanumeric characters.")
            print("💡 Make sure you've generated an App Password from Google Account settings.")
    
    # Read the settings file
    settings_file = "portfolio_django/settings.py"
    
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the EMAIL_HOST_PASSWORD
        pattern = r"EMAIL_HOST_PASSWORD = ''"
        replacement = f"EMAIL_HOST_PASSWORD = '{app_password}'"
        
        if pattern in content:
            updated_content = content.replace(pattern, replacement)
            
            # Write back to file
            with open(settings_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print("\n✅ Email configuration updated successfully!")
            print("📧 Email notifications will now be sent to: siddharthmishr125@gmail.com")
            print("\n🧪 To test the setup, run:")
            print("   python manage.py test_notifications --email-only")
            
        else:
            print("❌ Could not find EMAIL_HOST_PASSWORD in settings file.")
            print("Please manually update portfolio_django/settings.py")
            
    except FileNotFoundError:
        print(f"❌ Settings file not found: {settings_file}")
    except Exception as e:
        print(f"❌ Error updating settings: {e}")

def show_instructions():
    """Show detailed setup instructions"""
    
    print("\n📋 Detailed Setup Instructions:")
    print("=" * 40)
    print("\n1️⃣ Enable 2-Factor Authentication:")
    print("   • Go to https://myaccount.google.com/security")
    print("   • Click on '2-Step Verification'")
    print("   • Follow the steps to enable it")
    
    print("\n2️⃣ Generate App Password:")
    print("   • Go to https://myaccount.google.com/apppasswords")
    print("   • Select 'Mail' from the dropdown")
    print("   • Click 'Generate'")
    print("   • Copy the 16-character password")
    
    print("\n3️⃣ Update Settings:")
    print("   • Run this script: python setup_email.py")
    print("   • Or manually edit portfolio_django/settings.py")
    
    print("\n4️⃣ Test the Setup:")
    print("   • Run: python manage.py test_notifications --email-only")
    print("   • Submit a test contact form on your portfolio")

if __name__ == "__main__":
    print("🚀 Portfolio Email Notification Setup")
    print("=" * 40)
    
    choice = input("\nChoose an option:\n1. Update settings with app password\n2. Show detailed instructions\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        update_settings_file()
    elif choice == "2":
        show_instructions()
    else:
        print("❌ Invalid choice. Please run the script again.")



