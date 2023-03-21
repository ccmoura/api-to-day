from django.db import models

class Task(models.Model):
    class Meta:
        db_table = 'task'

    title = models.CharField(max_length=100)
    done = models.IntegerField()

    def __str__(self):
        return self.title