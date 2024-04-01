from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactform(models.Model):
  name = models.CharField(max_length = 50)
  subject = models.CharField(max_length = 50)
  email = models.EmailField(max_length = 150)
  message = models.TextField()

class bookingtable(models.Model):
  name = models.CharField(max_length = 50)
  email = models.EmailField(max_length = 150)
  date = models.DateField(null=True)
  people = models.IntegerField(null=True)
  timeslot = models.IntegerField(null=True)
  roomno = models.CharField(max_length = 50, null=True)
  message = models.TextField()

class cabdetailform(models.Model):
  name = models.CharField(max_length = 100)
  date = models.DateField(null=True)
  number = models.IntegerField()
  airport = models.CharField(max_length = 200)
  time = models.TimeField(null=True)
  
class testimonial(models.Model):
  name = models.CharField(max_length = 50)
  profession = models.CharField(max_length = 100)
  image = models.ImageField(upload_to="images\Testimonial")
  feedback = models.TextField()

class services(models.Model):
  name = models.CharField(max_length = 50)
  profession = models.CharField(max_length = 100)
  image = models.ImageField(upload_to="images\Service")
  feedback = models.TextField()
  
  
class team(models.Model):
  name = models.CharField(max_length = 100)
  designation = models.CharField(max_length = 150)
  image = models.ImageField(upload_to="images\Team")
  
class roomtesti(models.Model):
  name = models.CharField(max_length = 100)
  profession = models.CharField(max_length = 100)
  description = models.TextField()
  image = models.ImageField(upload_to="images\Room")
  
class roomtype(models.Model):
  image = models.ImageField(upload_to="images\Rooms")
  type = models.CharField(max_length = 100)
  price = models.IntegerField()
  beds = models.IntegerField()
  bath = models.IntegerField()
  wifi = models.CharField(max_length = 10)
  description = models.TextField()
  
class abouttesti(models.Model):
  image = models.ImageField(upload_to="images/About")
  name = models.CharField(max_length = 100)
  designation = models.CharField(max_length = 100)
  
class bookingdetailform(models.Model):
  name = models.CharField(max_length = 100 , null ="True")
  email = models.EmailField( null=True, default=None)
  checkin = models.DateField(null=True )
  checkout = models.DateField(null=True)
  adultnum = models.IntegerField()
  childnum = models.IntegerField(null=True)
  roomnum = models.IntegerField(null=True)
  request = models.TextField(null=True)
  
class Register(models.Model):
  fname = models.CharField(max_length = 100)
  lname = models.CharField(max_length = 100)
  email = models.EmailField(null=True)
  username = models.CharField(max_length = 100)
  password1 = models.CharField(max_length = 100)
  password2 = models.CharField(max_length = 100)

  def str(self): 
        return f"{self.name}"
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    birthdate = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField()

class eventdetailform(models.Model):
  # ename = models.CharField(max_length = 100)
  name = models.CharField(max_length = 100)
  email = models.EmailField(null=True)
  people = models.IntegerField()
  request = models.TextField()
  date = models.DateField(null=True)
  
  

    



  

  
  