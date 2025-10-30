from django.contrib import admin
from .models import Project, Contact, VisitorLog

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(VisitorLog)
