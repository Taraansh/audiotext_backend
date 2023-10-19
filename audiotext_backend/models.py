from django.db import models 

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


class Audio(models.Model):
    profile_linked = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='converted_file')
    converted_file = models.FileField(upload_to='converts/', null=True, blank=True)

    def __str__(self):
        return self.id