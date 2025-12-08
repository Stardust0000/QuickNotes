from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    text = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text[:30]