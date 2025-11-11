# 📧 Email Setup Guide - Get Gmail App Password

## 🚨 Current Issue
Your portfolio is trying to send emails but failing because the Gmail app password is not configured.

## ✅ Quick Fix Steps

### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Click on "2-Step Verification"
3. Follow the steps to enable it (if not already enabled)

### Step 2: Generate App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" from the dropdown menu
3. Click "Generate"
4. Copy the 16-character password (it looks like: `abcd efgh ijkl mnop`)

### Step 3: Update Settings File
1. Open `portfolio_django/settings.py` in your code editor
2. Find this line:
   ```python
   EMAIL_HOST_PASSWORD = 'your_16_character_app_password_here'
   ```
3. Replace `'your_16_character_app_password_here'` with your actual 16-character app password
4. Save the file

### Step 4: Test the Setup
Run this command to test:
```bash
python manage.py test_notifications --email-only
```

## 🔍 What Happens When Someone Contacts You

When someone submits the contact form on your portfolio:

1. **You get an email** to `siddharthmishr125@gmail.com` with:
   - Sender's name and email
   - Subject and full message
   - Professional HTML formatting

2. **They get a confirmation email** with:
   - Thank you message
   - Summary of their message
   - Your contact information

## 🧪 Test Your Contact Form

1. Go to your portfolio: http://127.0.0.1:8000/contact/
2. Fill out the contact form
3. Submit it
4. Check your email at `siddharthmishr125@gmail.com`

## 🔒 Security Note
- Never share your app password
- The app password is different from your regular Gmail password
- You can revoke app passwords anytime from Google Account settings

## 📞 Need Help?
If you're still having issues:
1. Make sure 2-Factor Authentication is enabled
2. Make sure you're using the app password (not your regular password)
3. Check that the 16-character password is copied correctly
4. Restart your Django server after updating the settings



