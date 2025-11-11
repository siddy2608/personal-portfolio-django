import os
import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from twilio.rest import Client
from twilio.base.exceptions import TwilioException

logger = logging.getLogger(__name__)

class NotificationService:
    """Service class for handling email and SMS notifications"""
    
    @staticmethod
    def send_email_notification(contact):
        """Send email notification for new contact form submission"""
        if not getattr(settings, 'ENABLE_EMAIL_NOTIFICATIONS', True):
            return False
            
        try:
            # Email to you (notification)
            subject = f"New Contact Form Submission: {contact.subject}"
            
            # HTML email template
            html_message = render_to_string('core/email/contact_notification.html', {
                'contact': contact,
                'site_name': 'Siddharth Portfolio'
            })
            
            # Plain text version
            plain_message = strip_tags(html_message)
            
            # Send email to you
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                html_message=html_message,
                fail_silently=False,
            )
            
            # Send confirmation email to the person who submitted the form
            confirmation_subject = "Thank you for contacting me!"
            confirmation_html = render_to_string('core/email/contact_confirmation.html', {
                'contact': contact,
                'site_name': 'Siddharth Portfolio'
            })
            confirmation_plain = strip_tags(confirmation_html)
            
            send_mail(
                subject=confirmation_subject,
                message=confirmation_plain,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                html_message=confirmation_html,
                fail_silently=False,
            )
            
            logger.info(f"Email notifications sent successfully for contact ID: {contact.id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email notification: {str(e)}")
            return False
    
    @staticmethod
    def send_sms_notification(contact):
        """Send SMS notification for new contact form submission"""
        if not getattr(settings, 'ENABLE_SMS_NOTIFICATIONS', True):
            return False
            
        # Check if Twilio credentials are configured
        if not all([
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN,
            settings.TWILIO_PHONE_NUMBER
        ]):
            logger.warning("Twilio credentials not configured. SMS notification skipped.")
            return False
            
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            
            message_body = (
                f"New contact form submission from {contact.name}!\n"
                f"Subject: {contact.subject}\n"
                f"Email: {contact.email}\n"
                f"Message: {contact.message[:100]}{'...' if len(contact.message) > 100 else ''}"
            )
            
            message = client.messages.create(
                body=message_body,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=settings.RECIPIENT_PHONE_NUMBER
            )
            
            logger.info(f"SMS notification sent successfully. SID: {message.sid}")
            return True
            
        except TwilioException as e:
            logger.error(f"Twilio SMS error: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Failed to send SMS notification: {str(e)}")
            return False
    
    @staticmethod
    def send_contact_notifications(contact):
        """Send both email and SMS notifications for a contact form submission"""
        email_sent = NotificationService.send_email_notification(contact)
        sms_sent = NotificationService.send_sms_notification(contact)
        
        return {
            'email_sent': email_sent,
            'sms_sent': sms_sent,
            'success': email_sent or sms_sent
        }

