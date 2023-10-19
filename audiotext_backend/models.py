from django.db import models 

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    converted_file = models.FileField(upload_to='converts/', null=True, blank=True)

    def __str__(self):
        return self.id