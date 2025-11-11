from django.db import models

    
class Task(models.Model):
    class Status(models.TextChoices):
            COMPLETED = 'C', 'Completed'
            PENDING = 'P', 'Pending'
            
    title = models.CharField(max_length = 200)
    body = models.TextField(null = True, blank = True)
    published = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length = 1,
        choices = Status.choices,
        default = Status.PENDING
    )
    changed = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title