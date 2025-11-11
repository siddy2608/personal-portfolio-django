from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education, Certification, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'location', 'available_for_work']
    search_fields = ['user__first_name', 'user__last_name', 'title']
    list_filter = ['available_for_work']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['name']
    ordering = ['category', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'completed_date']
    list_filter = ['category', 'featured', 'completed_date']
    search_fields = ['title', 'description']
    ordering = ['-featured', '-completed_date']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['position', 'company', 'description']
    ordering = ['-current', '-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['degree', 'institution', 'field_of_study']
    ordering = ['-current', '-start_date']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date']
    list_filter = ['issue_date', 'expiry_date']
    search_fields = ['name', 'issuing_organization']
    ordering = ['-issue_date']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} contact(s) marked as read.')
    mark_as_read.short_description = "Mark selected contacts as read"
    
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} contact(s) marked as unread.')
    mark_as_unread.short_description = "Mark selected contacts as unread"
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
