from django.contrib import admin

from .models import Employee_Registation


# Register your models here.

admin.site.register( Employee_Registation)

# hr/admin.py
from django.contrib import admin
from .models import HRRecord

class HRRecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'department', 'email')
    search_fields = ('first_name', 'last_name', 'job_title', 'department', 'email')
    list_filter = ('department', 'job_title', 'gender')

admin.site.register(HRRecord, HRRecordAdmin)

# hrleaves/admin.py
from django.contrib import admin
from .models import LeaveRecord

class LeaveRecordAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'leave_type', 'start_date', 'end_date', 'number_of_days', 'status', 'remaining_balance')
    search_fields = ('employee_name', 'leave_type', 'status')
    list_filter = ('leave_type', 'status')
admin.site.register(LeaveRecord, LeaveRecordAdmin)

# contact
