from django.db import models
import uuid
from django.utils import timezone

class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=500)
    body = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    CODE_LANGUAGES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('bash', 'Bash'),
        ('sql', 'SQL'),
        ('other', 'Other'),
    ]

    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    body = models.TextField()
    code = models.TextField(blank=True, null=True)  # Optional code snippet
    code_language = models.CharField(max_length=20, choices=CODE_LANGUAGES, default='python')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

