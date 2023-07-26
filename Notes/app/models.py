from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=500,blank=True,null=True)
    note = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

