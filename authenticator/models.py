from django.db import models

# tables
class Registered_logs(models.Model):    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[])
    contact = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

