from django.db import models

# Create your models here.


class Login_form(models.Model):
  email = models.CharField(max_length=30)
  upswd1 = models.CharField(max_length=30)
  

class New_Ticket(models.Model):
  Name = models.CharField(max_length=30)
  dept = models.CharField(max_length=30)
  category = models.CharField(max_length=30)
  subject = models.CharField(max_length=50)
  priority = models.CharField(max_length=30)
  description = models.CharField(max_length=100)
  
  