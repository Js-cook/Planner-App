from django.db import models

# Create your models here.
class Assignment(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  dt = models.DateTimeField()
  type = models.CharField(max_length=50, default="Assignment")
  completed = models.BooleanField(default=False)

  class Meta:
    ordering = ['-dt']
    
  def __str__(self):
    return self.title