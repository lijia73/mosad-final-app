from django.db import models

# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key = True)
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 20)

    Gender = models.CharField(max_length = 10, default = 'male')
    Region = models.CharField(max_length = 20, default = 'earth')
    Nickname = models.CharField(max_length = 20, default = 'fresh')
    Avatar = models.CharField(max_length = 100)
    # Avatar = models.ImageField(upload_to = 'avatar', storage = ImageStorage(), default = 'avatar/default.png') 

    Budget = models.IntegerField(default = 100000)

    def __str__(self):
        return self.Username
