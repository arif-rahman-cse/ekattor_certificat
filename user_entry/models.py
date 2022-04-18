from django.contrib.auth.models import User
from django.db import models

BLOOD_GROUP_CHOICES = (
    ('', '-- Select --'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

CARE_OF_CHOICES = (
    ('', '-- Select --'),
    ('Father', 'Father'),
    ('Husband', 'Husband'),
)

GENDER_CHOICES = (
    ('', '-- Select --'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)
RESIDENCE_CHOICES = (
    ('', '--Select--'),
    ('Permanent', 'Permanent'),
    ('Temporary', 'Temporary'),

)


# Create your models here.
class UserEntry(models.Model):

    # Personal Information
    name_en = models.CharField(max_length=200)
    name_bn = models.CharField(max_length=200)
    care_of = models.CharField(max_length=100, choices=CARE_OF_CHOICES)
    care_of_name_en = models.CharField(max_length=200, blank=True, null=True)
    care_of_name_bn = models.CharField(max_length=200, blank=True, null=True)
    mother_name_en = models.CharField(max_length=200, blank=True, null=True)
    mother_name_bn = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100)

    # Basic information
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP_CHOICES)
    nid_no = models.CharField(max_length=20, blank=True, null=True)
    birth_reg_no = models.CharField(max_length=20, blank=True, null=True)

    # Present Address
    present_address_en = models.CharField(max_length=200, blank=True, null=True)
    present_address_bn = models.CharField(max_length=200, blank=True, null=True)
    present_area_village_en = models.CharField(max_length=200, blank=True, null=True)
    present_area_village_bn = models.CharField(max_length=200, blank=True, null=True)
    present_division = models.CharField(max_length=100, blank=True, null=True)
    present_district = models.CharField(max_length=100, blank=True, null=True)
    present_thana = models.CharField(max_length=100, blank=True, null=True)
    present_post_office = models.CharField(max_length=100, blank=True, null=True)
    present_post_code = models.CharField(max_length=100, blank=True, null=True)
    residence_status = models.CharField(max_length=100, blank=True, null=True, choices=RESIDENCE_CHOICES)

    # Permanent Address
    permanent_address_en = models.CharField(max_length=200, blank=True, null=True)
    permanent_address_bn = models.CharField(max_length=200, blank=True, null=True)
    permanent_area_village_en = models.CharField(max_length=200, blank=True, null=True)
    permanent_area_village_bn = models.CharField(max_length=200, blank=True, null=True)
    permanent_division = models.CharField(max_length=100, blank=True, null=True)
    permanent_district = models.CharField(max_length=100, blank=True, null=True)
    permanent_thana = models.CharField(max_length=100, blank=True, null=True)
    permanent_post_office = models.CharField(max_length=100, blank=True, null=True)
    permanent_post_code = models.CharField(max_length=100, blank=True, null=True)

    # Document
    nid_birth_reg_image = models.ImageField(upload_to='nid_image', blank=True, null=True)
    user_image = models.ImageField(upload_to='user_image', blank=True, null=True)
    electricity_bill_image = models.ImageField(upload_to='electrical_bill_image', blank=True, null=True)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_by', blank=True, null=True)

    def __str__(self):
        return self.name_en


