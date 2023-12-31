# Generated by Django 3.2.20 on 2023-07-17 12:20

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=3000)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('gender', models.CharField(default='', max_length=20)),
                ('adress', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='DoctorModel',
            fields=[
                ('personmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hospital.personmodel')),
                ('specialization', models.CharField(default='', max_length=50)),
                ('degree', models.CharField(default='', max_length=50)),
                ('availability_status', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.departmentmodel')),
            ],
            options={
                'db_table': 'doctor',
            },
            bases=('hospital.personmodel',),
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('personmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hospital.personmodel')),
                ('medical_history', models.CharField(default='', max_length=9999)),
                ('status', models.BooleanField(default=False)),
                ('illness', models.CharField(default='', max_length=200)),
                ('assigned_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctormodel')),
            ],
            options={
                'db_table': 'patient',
            },
            bases=('hospital.personmodel',),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('roles', models.CharField(choices=[('a', 'Admin'), ('d', 'Doctor'), ('s', 'Stuff')], max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('personmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hospital.personmodel')),
                ('job', models.CharField(default='', max_length=99)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.departmentmodel')),
            ],
            options={
                'db_table': 'staff',
            },
            bases=('hospital.personmodel',),
        ),
        migrations.CreateModel(
            name='PrescriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('medication', models.CharField(default='', max_length=299)),
                ('dosage', models.CharField(default='', max_length=123)),
                ('instructions', models.CharField(default='', max_length=1234)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctormodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patientmodel')),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
        migrations.CreateModel(
            name='Medical_ReccordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(default='', max_length=3030)),
                ('treatment', models.CharField(default='', max_length=2023)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patientmodel')),
            ],
            options={
                'db_table': 'medical',
            },
        ),
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_time', models.DateTimeField(default=datetime.datetime)),
                ('A_date', models.DateField(default=datetime.datetime)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctormodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patientmodel')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
