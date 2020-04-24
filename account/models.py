from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Gender = [
    ('Male','male'),
    ('Female','female'),
    ('Other','other'),
]

class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=Gender,default="Male")
    dob = models.DateField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username