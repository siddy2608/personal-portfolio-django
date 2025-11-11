# 🔐 Credentials Setup Guide

## 📧 Email Configuration (Gmail)

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification
3. Enable 2-Step Verification if not already enabled

### Step 2: Generate App Password
1. Go to Google Account settings
2. Navigate to Security → App passwords
3. Select "Mail" as the app
4. Generate a 16-character app password
5. Copy the generated password

### Step 3: Update Django Settings
Open `portfolio_django/settings.py` and replace the empty `EMAIL_HOST_PASSWORD` with your app password:

```python
EMAIL_HOST_PASSWORD = 'your_16_character_app_password_here'
```

## 📱 SMS Configuration (Twilio)

### Step 1: Create Twilio Account
1. Go to [twilio.com](https://twilio.com)
2. Sign up for a free account
3. Verify your email and phone number

### Step 2: Get Credentials
1. Go to Twilio Console
2. Copy your Account SID
3. Copy your Auth Token
4. Get a Twilio phone number (free trial includes one)

### Step 3: Update Django Settings
Open `portfolio_django/settings.py` and update these values:

```python
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token_here'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here'
```

## 🧪 Testing the Setup

After updating the credentials, test the system:

```bash
# Test email only
python manage.py test_notifications --email-only

# Test SMS only
python manage.py test_notifications --sms-only

# Test both
python manage.py test_notifications
```

## 🔒 Security Notes

- Never commit your actual credentials to version control
- Use environment variables in production
- Keep your app passwords and Twilio tokens secure
- Regularly rotate your credentials

## 📞 Support

If you need help setting up:
1. Check the `NOTIFICATION_SETUP.md` file for detailed instructions
2. Visit the contact form on your portfolio to test the system
3. Check the Django admin at `/admin/` to view contact submissions



