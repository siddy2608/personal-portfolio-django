# Email and SMS Notification Setup Guide

This guide will help you configure email and SMS notifications for your Django portfolio contact form.

## 📧 Email Configuration (Gmail)

### 1. Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Navigate to Security
3. Enable 2-Step Verification

### 2. Generate App Password
1. Go to Google Account settings
2. Navigate to Security → 2-Step Verification
3. Click on "App passwords"
4. Generate a new app password for "Mail"
5. Copy the 16-character password

### 3. Update Django Settings
Edit `portfolio_django/settings.py` and update the email configuration:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'siddharthmishr125@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'your-16-character-app-password'  # App password from step 2
DEFAULT_FROM_EMAIL = 'siddharthmishr125@gmail.com'
```

## 📱 SMS Configuration (Twilio)

### 1. Create Twilio Account
1. Go to [Twilio.com](https://www.twilio.com)
2. Sign up for a free account
3. Verify your phone number

### 2. Get Twilio Credentials
1. Go to your Twilio Console
2. Copy your Account SID and Auth Token
3. Get a Twilio phone number (free trial includes one)

### 3. Update Django Settings
Edit `portfolio_django/settings.py` and update the SMS configuration:

```python
# Twilio SMS Configuration
TWILIO_ACCOUNT_SID = 'your-account-sid'
TWILIO_AUTH_TOKEN = 'your-auth-token'
TWILIO_PHONE_NUMBER = '+1234567890'  # Your Twilio phone number
RECIPIENT_PHONE_NUMBER = '+919936057425'  # Your phone number for notifications
```

## 🔧 Testing the Configuration

### Test Email Only
```bash
python manage.py test_notifications --email-only
```

### Test SMS Only
```bash
python manage.py test_notifications --sms-only
```

### Test Both
```bash
python manage.py test_notifications
```

## 🚀 How It Works

### When someone submits the contact form:

1. **Email to You**: You'll receive a detailed notification email with:
   - Contact information (name, email, subject)
   - Full message content
   - Timestamp

2. **Confirmation Email**: The person who submitted the form receives:
   - Thank you message
   - Message summary
   - Your contact information
   - Next steps

3. **SMS Notification**: You'll receive a text message with:
   - Sender's name
   - Subject
   - Email address
   - First 100 characters of the message

## 🔒 Security Notes

- **Never commit credentials to version control**
- Use environment variables for production:
  ```python
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
  TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
  TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
  ```

## 📝 Environment Variables (Recommended)

Create a `.env` file in your project root:

```env
EMAIL_HOST_PASSWORD=your-gmail-app-password
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+1234567890
```

Then install python-dotenv and update settings:

```bash
pip install python-dotenv
```

Add to `settings.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
```

## 🛠️ Troubleshooting

### Email Issues
- Check if 2FA is enabled on Gmail
- Verify app password is correct
- Ensure Gmail allows "less secure app access" (if not using app password)

### SMS Issues
- Verify Twilio account is active
- Check if phone numbers are in correct format (+1234567890)
- Ensure you have credits in your Twilio account

### General Issues
- Check Django logs for detailed error messages
- Verify all settings are correctly configured
- Test with the management command first

## 📞 Support

If you encounter issues:
1. Check the Django logs
2. Run the test command to identify the problem
3. Verify your credentials are correct
4. Ensure your email/SMS providers are working



