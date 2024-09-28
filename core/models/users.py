from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Docente', 'Docente'),
        ('Alumno', 'Alumno'),
    )
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

