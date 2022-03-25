from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    sex = models.CharField(max_length=1)
    mail = models.EmailField()
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.surname
