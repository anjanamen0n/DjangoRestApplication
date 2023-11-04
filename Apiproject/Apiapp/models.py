
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patient_Records(models.Model):
    Record_id = models.BigAutoField(primary_key=True)
    Patient_id = models.ForeignKey(User, verbose_name="patient",related_name="patient_records", on_delete=models.CASCADE)
    Doctor_id = models.ForeignKey(User, verbose_name="Doctor",related_name="Doctor_records", on_delete=models.CASCADE,null=True)
    Created_date = models.DateField(auto_now_add=True)
    Diagnostics = models.TextField()
    Observations = models.TextField()
    Treatments = models.TextField()
    department = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    idMisc = models.TextField(verbose_name="Miscellaneous", default='')

    def __str__(self):
        return f"Record id: {self.Record_id}"

    class Meta:
        verbose_name_plural="Patient_Records"

class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Departments"
    
    

