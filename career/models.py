from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Opportunity(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = [
        ('internship', 'Internship'),
        ('job', 'Job'),
        ('hackathon', 'Hackathon'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    is_paid = models.BooleanField(default=False)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.company}"

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.opportunity.title}"

class MockTest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.URLField()
    
    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=User)
def handle_user_save(sender, instance, **kwargs):
    if not instance.pk and instance.password:
        # This is a new user being created
        instance._state.adding = True
    else:
        # This is an existing user being updated
        instance._state.adding = False