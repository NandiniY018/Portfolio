"""
website/models.py
Database models for the portfolio website.
"""
from django.db import models


class ContactMessage(models.Model):
    """Stores messages submitted via the contact form."""
    name = models.CharField(max_length=150, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email Address')
    subject = models.CharField(max_length=250, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Received At')
    is_read = models.BooleanField(default=False, verbose_name='Read')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.subject} ({self.created_at.strftime('%d %b %Y')})"
