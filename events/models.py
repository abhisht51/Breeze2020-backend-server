from datetime import datetime
from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your models here.

class Accommodation(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100,default="Shiv Nadar University")
    start_date = models.PositiveIntegerField()
    # DateField()
    #package_type = models.CharField(max_length=100)
    CHOICES = (
        ('1', '1 day'),
        ('2', '2 days'),
        ('3', '3 days'),
        ('4', '4 days'),

    )
    amount= models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=CHOICES)
    include_food = models.CharField(max_length=10) 
    mobile_no=models.CharField(max_length=100,help_text='Contact number of guests ',null=True)
    number_of_people = models.IntegerField(default=1)
    paid = models.CharField(default="Unpaid",help_text="Paid,Verification pending or Unpaid.If verified change to paid",max_length=25)
    class Meta:
        db_table = 'Accommodation'
    
    def users_name(self):
        user = User.objects.filter(id=self.user_id).values()[0]
        return (user.get("first_name") + " " + user.get("last_name"))


class Event_Registrations(models.Model):
    user_id=models.PositiveIntegerField()
    event_id=models.PositiveIntegerField()
    event_name=models.CharField(max_length=100)
    amount= models.PositiveIntegerField(null=True)
    paid = models.CharField(default="Unpaid",help_text="Paid,Verification pending or Unpaid.If verified change to paid",max_length=25)
    payment_id = models.CharField(max_length=300, default="")
    form_array=models.TextField(default="")
    numberofpeople=models.PositiveIntegerField(default=1)
    perperson=models.BooleanField(default=False)
    class Meta:
        db_table = 'Event_Registrations'
    
    def __str__(self):
        stre = self.event_name + " : " + self.paid
        return stre

    def users_name(self):
        user = User.objects.filter(id=self.user_id).values()[0]
        return (user.get("first_name") + " " + user.get("last_name"))
    
    def college(self):
        user = User.objects.filter(id=self.user_id).values()[0]
        return user.get("college")

class Payment(models.Model):
    user_id=models.PositiveIntegerField()
    uuid = models.CharField(max_length=300, null=True)
    name=models.CharField(max_length=1000)
    college=models.CharField(max_length=1000, default="Shiv Nadar University")
    events=models.CharField(max_length=1000)
    payment_string = models.CharField(max_length=200, null=True)
    partial=models.BooleanField(default=False)
    fullAmount=models.PositiveIntegerField(null=True)
    amount=models.PositiveIntegerField(null=True)
    paid=models.CharField(default="Verification Pending",help_text="Verification Pending or Paid. If verified change to paid",max_length=25)
    class Meta:
        db_table = 'Payments'
    
    def __str__(self):
        stre = self.name + " : " + self.paid
        return stre

class Cultural_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    sheet_link=models.CharField(max_length=100, null=True)
    time=models.CharField(max_length=100)
    description=models.TextField(null=True)
    category=models.CharField(max_length=100,help_text='Examples: music,dance',null=True)
    club=models.CharField(max_length=100,null=True)
    rules=models.TextField(null=True)

    fees_snu=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    fees_amount=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    prize_money=models.TextField(null=True)
    team_size_min=models.IntegerField(default=1, null=True)
    team_size_max=models.IntegerField(default=1, null=True)
    perperson=models.BooleanField(default=False)
    form_array=models.TextField(default="")
    time_limit=models.CharField(max_length=100,help_text='Time limit for one performance or event if not then enter null',null=True)
    registration_link=models.CharField(max_length=200,null=True)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative',null=True)
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative',null=True)
    poster=models.ImageField(upload_to='static/static_dirs/images/',help_text='Poster file',null=True)
    offsite_register = models.BooleanField(default=False)
    offsite_register_link = models.CharField(max_length=600,null=True)

    class Meta:
        db_table = 'Cultural_Events'
    
    def __str__(self):
        return '%s by %s' % (self.name, self.club)

class Technical_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    sheet_link=models.CharField(max_length=100, null=True)
    time=models.CharField(max_length=100)
    description=models.TextField(null=True)
    category=models.CharField(max_length=100,help_text='Examples: music,dance',null=True)
    club=models.CharField(max_length=100,null=True)
    rules=models.TextField(null=True)
    fees_snu=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    fees_amount=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    prize_money=models.TextField(null=True)
    team_size_min=models.IntegerField(default=1, null=True)
    team_size_max=models.IntegerField(default=1, null=True)
    perperson=models.BooleanField(default=False)
    form_array=models.TextField(default="")
    time_limit=models.CharField(max_length=100,help_text='Time limit for one event if not then enter null',null=True)
    registration_link=models.CharField(max_length=200,null=True)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative',null=True)
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative',null=True)
    poster=models.ImageField(upload_to='static/static_dirs/images/',help_text='Poster file',null=True)
    offsite_register = models.BooleanField(default=False)
    offsite_register_link = models.CharField(max_length=600,null=True)
    class Meta:
        db_table = 'Technical_Events'
        
    def __str__(self):
        return '%s by %s' % (self.name, self.club)

class Sports_Events(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    sheet_link=models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=100,help_text='Examples: music,dance',null=True)
    time=models.CharField(max_length=100)
    description=models.TextField(null=True)
    fees_amount=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    rules=models.TextField(null=True)
    prize_money=models.TextField(null=True)
    team_size_min=models.IntegerField(default=1, null=True)
    team_size_max=models.IntegerField(default=1, null=True)
    form_array=models.TextField(default="")
    perperson=models.BooleanField(default=True)
    fees_snu=models.DecimalField(decimal_places=2,max_digits=9,null=True)
    registration_link=models.CharField(max_length=200,null=True)
    person_of_contact=models.CharField(max_length=100,help_text='Name of person representative',null=True)
    person_of_contactno=models.CharField(max_length=100,help_text='Contact number of person representative',null=True)
    poster=models.ImageField(upload_to='static/static_dirs/images/',help_text='Poster file',null=True)
    offsite_register = models.BooleanField(default=False)
    offsite_register_link = models.CharField(max_length=600,null=True)
    class Meta:
        db_table = 'Sports_Events'

    def __str__(self):
        return '%s' % (self.name)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address!')

        if not password:
            raise ValueError('Users must have a password!')

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.save(using = self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user      


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True) # can log in
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    uuid=models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(default=datetime.now)
    mobile_num = models.CharField(max_length=10,null=True)
    college = models.CharField(max_length=100,default="Shiv Nadar University")
    
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = [] #USERNAME_FIELD and Password required by default.

    objects = UserManager()

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    # # def save(self, *args, **kwargs):
    # #     self.subscription_end = date.today() + relativedelta(months=+self.subscription_period)
    # #     super(User, self).save(*args, **kwargs) # Call the "real" save() method.

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
