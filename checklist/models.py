from django.db import models

class ChecklistItem(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task