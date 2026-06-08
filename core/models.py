from django.db import models

class ContactMessage(models.Model):
    """Stores messages sent via the contact form."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at.strftime('%d %b %Y')})"


class Project(models.Model):
    """Showcase projects for the Our Projects page."""
    CATEGORY_CHOICES = [
        ('it', 'IT Solutions'),
        ('electrical', 'Electrical Engineering'),
        ('security', 'Security Systems'),
        ('telecom', 'Telecommunications'),
        ('maintenance', 'Maintenance'),
        ('consulting', 'Consulting & Design'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    client = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    class Meta:
        ordering = ['-year', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.client})"


class TeamMember(models.Model):
    """Team members for the Our Team page."""
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    bio = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} — {self.role}"


class JobOpening(models.Model):
    """Job openings for the Careers page."""
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Dar es Salaam, Tanzania')
    type = models.CharField(max_length=50, default='Full-time')
    description = models.TextField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f"{self.title} — {self.department}"


class NewsPost(models.Model):
    """News/blog posts for the News page."""
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100, default='TESTECH Team')
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news_detail', kwargs={'slug': self.slug})