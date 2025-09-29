from django.db import models

class vecancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    experience = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    isopen=models.BooleanField(default=True)

class applicant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey(vecancy, on_delete=models.CASCADE)
    
class interviewers(models.Model):
    name = models.CharField(max_length=255)


class interview(models.Model):
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(interviewers, on_delete=models.CASCADE)
    scheduled_on = models.DateTimeField()
    feedback = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled') 