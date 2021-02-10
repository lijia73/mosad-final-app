from django.db import models

# Create your models here.

class Record(models.Model):
    RecordID = models.CharField(primary_key = True,max_length = 24)
    Type = models.CharField(max_length = 20)
    Time = models.CharField(max_length = 20)

    Ownusername = models.CharField(max_length = 20)
    Amount = models.IntegerField()
    Comment = models.CharField(max_length = 20)
	
    Class = models.BooleanField(default = True)

    def __str__(self):
        return self.RecordID