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

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Main thumbnail image")
    icon_class = models.CharField(max_length=50, default='fas fa-code')
    icon_color = models.CharField(max_length=20, default='#6366f1', help_text="Hex color code (e.g. #6366f1)")
    github_link = models.URLField(blank=True)
    features = models.TextField(help_text="Newline-separated features", blank=True)
    tech_stack = models.TextField(help_text="Comma-separated technologies", blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_features_list(self):
        # We try splitting by newline first, if no newlines exist we fallback to comma for backwards compatibility,
        # but wait, if we fallback to comma, the user's current issue with commas in a single line sentence will still fail!
        # Actually, let's just split by newline ONLY. If they have commas from old entries, they'll just become one bullet, which they can fix by pressing enter.
        # But wait, what if we split by newline if there are any newlines, else if there are NO newlines, we return it as a SINGLE bullet.
        # Yes, splitting by \n is the standard.
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def get_tech_stack_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/', help_text="Project screenshot or demo image")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption for this image")
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — Image {self.order}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, help_text="e.g. Programming Languages, Frontend, Backend, Tools")
    category_order = models.IntegerField(default=0, help_text="Lower numbers appear first (e.g. 1 for Frontend, 2 for Backend)")
    category_icon_class = models.CharField(max_length=50, default='fas fa-layer-group', help_text="FontAwesome class for the category")
    percentage = models.IntegerField(default=0)
    icon_class = models.CharField(max_length=50, default='fas fa-code', help_text="FontAwesome class e.g. fab fa-python")
    icon_color = models.CharField(max_length=20, default='#06b6d4', help_text="Hex color code (e.g. #f0db4f for JS)")
    order = models.IntegerField(default=0, help_text="Order of this skill within its category")

    class Meta:
        ordering = ['category_order', 'category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.CharField(max_length=50, help_text="e.g. Mar 2026")
    end_date = models.CharField(max_length=50, help_text="e.g. June 2026 or Present")
    description = models.TextField(help_text="Newline separated bullet points")
    icon_class = models.CharField(max_length=50, default='fas fa-laptop-code', help_text="FontAwesome class e.g. fas fa-briefcase")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"

    def get_description_list(self):
        return [d.strip() for d in self.description.split('\n') if d.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=150, help_text="e.g. Bachelor of Engineering (BE)")
    field_of_study = models.CharField(max_length=150, help_text="e.g. Computer Science")
    institution = models.CharField(max_length=200)
    GRADE_CHOICES = (
        ('CGPA', 'CGPA'),
        ('Percentage', 'Percentage'),
        ('', 'None')
    )
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    grade_type = models.CharField(max_length=20, choices=GRADE_CHOICES, default='', blank=True)
    grade = models.CharField(max_length=100, blank=True, help_text="e.g. 8.4 or 77")
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=50, default='fas fa-graduation-cap', help_text="FontAwesome class e.g. fas fa-school")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    url = models.URLField(help_text="Link to the full article (e.g. Medium, Dev.to)")
    published_date = models.DateField()
    read_time = models.CharField(max_length=50, default="5 min read")
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    tags = models.CharField(max_length=200, help_text="Comma-separated tags", blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class SiteSettings(models.Model):
    """Singleton model for SEO and global settings"""
    seo_title = models.CharField(max_length=150, default="Nandini Y. | Python Full Stack Developer")
    seo_description = models.TextField(default="Python Full Stack Developer specializing in Django, React, MySQL, and REST APIs.")
    seo_keywords = models.TextField(default="Python developer, Full Stack Developer, Django, React, MySQL, portfolio, Nandini")
    seo_image = models.ImageField(upload_to='seo/', blank=True, null=True)
    google_analytics_id = models.CharField(max_length=50, blank=True, help_text="e.g. G-XXXXXXXXXX")
    
    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return "Global Site Settings"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=150, help_text="e.g. Certification, Internship Certificate")
    institution = models.CharField(max_length=200, help_text="e.g. NIIT / Udemy")
    duration = models.CharField(max_length=100, help_text="e.g. 6 Months · 2025")
    description = models.TextField()
    tech_stack = models.CharField(max_length=250, help_text="Comma-separated technologies", blank=True)
    icon_class = models.CharField(max_length=50, default='fas fa-certificate')
    color_start = models.CharField(max_length=20, default='#6366f1', help_text="Hex code, e.g. #6366f1")
    color_end = models.CharField(max_length=20, default='#8b5cf6', help_text="Hex code, e.g. #8b5cf6")
    text_color_class = models.CharField(max_length=50, default='text-primary-400', help_text="Tailwind class, e.g. text-primary-400")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True, help_text="Upload certificate image")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.category})"
    def get_tech_stack_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Resume(models.Model):
    file = models.FileField(upload_to='resume/', help_text="Upload your resume (PDF, DOCX, etc.)")
    is_active = models.BooleanField(default=True, help_text="Make this the active resume shown on the website")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"Resume uploaded on {self.uploaded_at.strftime('%d %b %Y')} ({status})"

    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other resumes to inactive
            Resume.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
