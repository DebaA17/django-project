from django.db import models

# Profile model for About, Skills, Education, Achievements, Social links
class Profile(models.Model):
    name = models.CharField(max_length=100, default='Your Name')
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True, help_text='Comma-separated list')
    education = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    social_links = models.TextField(blank=True, help_text='Comma-separated: label|url')

    def get_skills(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def get_social_links(self):
        # Format: label|url,label|url
        links = []
        for item in self.social_links.split(','):
            if '|' in item:
                label, url = item.split('|', 1)
                links.append({'label': label.strip(), 'url': url.strip()})
        return links


    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# New model to log visitor info
class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField()
    isp = models.CharField(max_length=255, blank=True)
    system = models.CharField(max_length=255, blank=True)
    browser = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"
