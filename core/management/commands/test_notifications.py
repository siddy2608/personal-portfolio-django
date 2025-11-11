from django.core.management.base import BaseCommand
from django.conf import settings
from core.services import NotificationService
from core.models import Contact
from datetime import datetime


class Command(BaseCommand):
    help = 'Test email and SMS notification functionality'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email-only',
            action='store_true',
            help='Test only email notifications',
        )
        parser.add_argument(
            '--sms-only',
            action='store_true',
            help='Test only SMS notifications',
        )

    def handle(self, *args, **options):
        self.stdout.write('Testing notification system...')
        
        # Create a test contact
        test_contact = Contact.objects.create(
            name='Test User',
            email='test@example.com',
            subject='Test Notification',
            message='This is a test message to verify that the notification system is working properly.',
            created_at=datetime.now()
        )
        
        try:
            if options['email_only']:
                self.stdout.write('Testing email notifications...')
                email_sent = NotificationService.send_email_notification(test_contact)
                if email_sent:
                    self.stdout.write(
                        self.style.SUCCESS('✅ Email notification sent successfully!')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR('❌ Email notification failed!')
                    )
                    
            elif options['sms_only']:
                self.stdout.write('Testing SMS notifications...')
                sms_sent = NotificationService.send_sms_notification(test_contact)
                if sms_sent:
                    self.stdout.write(
                        self.style.SUCCESS('✅ SMS notification sent successfully!')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR('❌ SMS notification failed!')
                    )
                    
            else:
                self.stdout.write('Testing both email and SMS notifications...')
                result = NotificationService.send_contact_notifications(test_contact)
                
                if result['email_sent']:
                    self.stdout.write(
                        self.style.SUCCESS('✅ Email notification sent successfully!')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR('❌ Email notification failed!')
                    )
                    
                if result['sms_sent']:
                    self.stdout.write(
                        self.style.SUCCESS('✅ SMS notification sent successfully!')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR('❌ SMS notification failed!')
                    )
                    
                if result['success']:
                    self.stdout.write(
                        self.style.SUCCESS('🎉 Notification test completed!')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING('⚠️ Some notifications failed. Check your configuration.')
                    )
                    
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Test failed with error: {str(e)}')
            )
            
        finally:
            # Clean up test contact
            test_contact.delete()
            
        # Display configuration status
        self.stdout.write('\n📋 Configuration Status:')
        self.stdout.write(f'Email notifications enabled: {getattr(settings, "ENABLE_EMAIL_NOTIFICATIONS", True)}')
        self.stdout.write(f'SMS notifications enabled: {getattr(settings, "ENABLE_SMS_NOTIFICATIONS", True)}')
        self.stdout.write(f'Email host: {getattr(settings, "EMAIL_HOST", "Not configured")}')
        self.stdout.write(f'Email user: {getattr(settings, "EMAIL_HOST_USER", "Not configured")}')
        self.stdout.write(f'Twilio configured: {bool(getattr(settings, "TWILIO_ACCOUNT_SID", None))}')
        self.stdout.write(f'Recipient phone: {getattr(settings, "RECIPIENT_PHONE_NUMBER", "Not configured")}')



