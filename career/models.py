from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone


class Opportunity(models.Model):
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

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return f"{self.title} - {self.company}"


class Application(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    resume = models.FileField(
        upload_to='resumes/%Y/%m/%d/',
        help_text='Upload your resume (PDF, DOC, DOCX only)',
    )
    applied_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('reviewing', 'Reviewing'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )

    class Meta:
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.name} - {self.opportunity.title}"

    def clean(self):
        # Add any custom validation here
        if self.opportunity.deadline < timezone.now().date():
            raise ValidationError("This opportunity is no longer accepting applications.")


class MockTest(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title