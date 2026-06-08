from django.contrib import admin
from .models import ContactMessage, Project, TeamMember, JobOpening, NewsPost
# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(JobOpening)
admin.site.register(NewsPost)