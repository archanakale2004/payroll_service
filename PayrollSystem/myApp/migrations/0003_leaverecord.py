# Generated by Django 5.0.6 on 2024-06-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_hrrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=100)),
                ('leave_type', models.CharField(choices=[('Vacation', 'Vacation'), ('Sick Leave', 'Sick Leave'), ('Maternity Leave', 'Maternity Leave'), ('Personal Leave', 'Personal Leave')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], max_length=10)),
                ('remaining_balance', models.IntegerField()),
            ],
        ),
    ]
