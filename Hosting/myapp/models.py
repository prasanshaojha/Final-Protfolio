from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('BLOG', 'Blog'),
        ('R_CODE', 'R Source Code'),
        ('STATA_CODE', 'Stata Source Code'),
        ('RESEARCH', 'Research Paper'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)  # For blogs and research papers
    code = models.TextField(blank=True, null=True)  # For R or Stata source code
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.get_content_type_display()} | {self.author}"
    
class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} ({self.email})"
