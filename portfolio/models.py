from django.db import models

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
