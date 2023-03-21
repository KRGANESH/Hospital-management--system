from django.db import models

# Create your models here.
class patient_details(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.name

class doctor_details(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    specialization=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class lab_technician(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    def __str__(self):
        return self.name


class appointment(models.Model):
    doctor_name=models.CharField(max_length=50)
    patient_name=models.CharField(max_length=50)
    doctor_username=models.CharField(max_length=50)
    patient_username=models.CharField(max_length=50)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    prescription=models.CharField(max_length=200)
    test_name=models.CharField(max_length=50,null=True)
    report=models.FileField(upload_to='reports',null=True)
    status=models.BooleanField()

    def __str__(self ):
        return self.patient_name+" have appointment with "+self.doctor_name

class lab_tests(models.Model):
    test_name=models.CharField(max_length=50)

    def __str__(self):
        return self.test_name
    


    
    

