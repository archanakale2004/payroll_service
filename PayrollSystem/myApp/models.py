from django.db import models

# Create your models here.
class Employee_Registation(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email_id= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    password= models.CharField(max_length=60)
    confirm_password= models.CharField(max_length=60) 

   # hr/models.py
from django.db import models

class HRRecord(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    leave_balance = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# hrleaves/models.py
from django.db import models

class LeaveRecord(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Vacation', 'Vacation'),
        ('Sick Leave', 'Sick Leave'),
        ('Maternity Leave', 'Maternity Leave'),
        ('Personal Leave', 'Personal Leave'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    ]
   
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_days = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    remaining_balance = models.IntegerField()

    def __str__(self):
        return f"{self.employee_name} - {self.leave_type}"

# Optionally, you might want to add metadata and custom methods to your model.
#leaves balance 

