from django.db import models
from django import forms
# Create your models here.


class number(models.Model):
    number = models.BigIntegerField(max_length=11)
    def __str__(self):
        return self.number


class plan(models.Model):
    plan_name = models.CharField(max_length=100)
    usage = models.FloatField(max_length=100)
    validity = models.IntegerField(max_length=100)
    amount = models.IntegerField(max_length=100)
    def __str__(self):
        return self.plan_name, self.usage, self.validity, self.amount


class account(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.BigIntegerField(max_length=10)
    account_ID = models.IntegerField(max_length=100)
    service = models.CharField(max_length=50)
    def __str__(self):
        return self.name, self.email, self.number, self.account_ID, self.service



class dueamt(models.Model):
    amtdue= models.IntegerField(max_length=100)
    def __str__(self):
        return self.amtdue


class prepaid(models.Model):
    cost = models.CharField(max_length=100)
    data_day = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.cost, self.data_day, self.validity, self.desc


class postpaid(models.Model):
    cost = models.CharField(max_length=100)
    total_data = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.cost, self.total_data, self.validity, self.desc


class dongle(models.Model):
    cost = models.CharField(max_length=100)
    data_day = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.cost, self.data_day, self.validity, self.desc


class recharge(models.Model):
    number = models.BigIntegerField(max_length=11)
    plan = models.CharField(max_length=100)
    amt = models.IntegerField(max_length=10)
    def __str__(self):
        return self.number, self.plan, self.amt


class buy(models.Model):
  cust_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  number = models.BigIntegerField(max_length=11)
  address= models.CharField(max_length=100)
  datetime = models.DateTimeField(help_text = "mm/dd/yy Hour:Min")
  type = models.CharField(max_length=100, help_text="small case please")
  def __str__(self):
    return self.name, self.number, self.address, self.datetime


class recharging(models.Model):
    cust_id=models.AutoField(primary_key=True)
    number = models.BigIntegerField(max_length=11)
    type = models.CharField(max_length=100, help_text="small case please" )
    amt = models.IntegerField()
    def __str__(self):
      return self.number, self.type, self.amt

class issue(models.Model):
    issue_type = models.CharField(max_length=20)
    Describe_your_issue = models.TextField(max_length=1000)
    def __str__(self):
      return self.issue_type, self.Describe_your_issue


class invoice(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField(max_length=11)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    def __str__(self):
      return self.name, self.number, self.email, self.city

