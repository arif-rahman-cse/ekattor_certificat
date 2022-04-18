from django.contrib.auth.models import User
from django import forms

from user_entry.models import UserEntry


class UserEntryCreateForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = (
            'name_en', 'name_bn', 'care_of', 'care_of_name_en', 'care_of_name_bn', 'mother_name_en', 'mother_name_bn',
            'email', 'phone', 'date_of_birth', 'gender', 'blood_group', 'nid_no', 'birth_reg_no', 'present_address_en',
            'present_address_bn', 'present_area_village_en', 'present_area_village_bn', 'present_division',
            'present_district', 'present_thana', 'present_post_office', 'present_post_code', 'residence_status',
            'permanent_address_en', 'permanent_address_bn', 'permanent_area_village_en', 'permanent_area_village_bn',
            'permanent_division', 'permanent_district', 'permanent_thana', 'permanent_post_office',
            'permanent_post_code', 'nid_birth_reg_image', 'user_image', 'electricity_bill_image', 'status',
            'created_by',)

        widgets = {
            # Personal Information
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'name_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'care_of': forms.Select(attrs={'class': 'form-control'}),
            'care_of_name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'care_of_name_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'mother_name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'mother_name_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            # Basic information
            'date_of_birth': forms.DateTimeInput(format='%Y-%m-%d',
                                                 attrs={'required': True, 'class': 'form-control', 'type': 'date', }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'nid_no': forms.NumberInput(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),
            'birth_reg_no': forms.NumberInput(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),

            # Present Address
            'present_address_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'present_address_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'present_area_village_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'present_area_village_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'present_division': forms.Select(attrs={'class': 'form-control'}),
            'present_district': forms.Select(attrs={'class': 'form-control'}),
            'present_thana': forms.Select(attrs={'class': 'form-control'}),
            'present_post_office': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'present_post_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'residence_status': forms.Select(attrs={'class': 'form-control'}),

            # Permanent Address
            'permanent_address_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_address_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_division': forms.Select(attrs={'class': 'form-control'}),
            'permanent_district': forms.Select(attrs={'class': 'form-control'}),
            'permanent_thana': forms.Select(attrs={'class': 'form-control'}),
            'permanent_post_office': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_post_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),

            # Document
            'nid_birth_reg_image': forms.FileInput(attrs={'class': 'form-control'}),
            'user_image': forms.FileInput(attrs={'class': 'form-control'}),
            'electricity_bill_image': forms.FileInput(attrs={'class': 'form-control'}),

        }

        labels = {
            # Personal Information
            'name_en': 'Name (English)',
            'name_bn': 'Name (Bangla)',
            'care_of': 'Care of',
            'care_of_name_en': 'Care of Name (English)',
            'care_of_name_bn': 'Care of Name (Bangla)',
            'mother_name_en': 'Mother Name (English)',
            'mother_name_bn': 'Mother Name (Bangla)',
            'email': 'Email',
            'phone': 'Phone Number',

            # Basic information
            'date_of_birth': 'Date of Birth',
            'gender': 'Select Gender',
            'blood_group': 'Select Blood Group',
            'nid_no': 'NID Number English 10 to 17 digits',
            'birth_reg_no': 'Birth Certificate Number English 10 to 17 digits',

            # Present Address
            'present_address_en': 'Address (English)',
            'present_address_bn': 'Address (Bangla)',
            'present_area_village_en': 'Area/Village (English)',
            'present_area_village_bn': 'Area/Village (Bangla)',
            'present_division': 'Division',
            'present_district': 'District',
            'present_thana': 'Thana',
            'present_post_office': 'Post Office',
            'present_post_code': 'Post Code',
            'residence_status': 'Residence Status',

            # Permanent Address
            'permanent_address_en': 'Address (English)',
            'permanent_address_bn': 'Address (Bangla)',
            'permanent_area_village_en': 'Area/Village (English)',
            'permanent_area_village_bn': 'Area/Village (Bangla)',
            'permanent_division': 'Division',
            'permanent_district': 'District',
            'permanent_thana': 'Thana',
            'permanent_post_office': 'Post Office',
            'permanent_post_code': 'Post Code',

            # Document
            'nid_birth_reg_image': 'NID/Birth Certificate Image',
            'user_image': 'User Personal Image',
            'electricity_bill_image': 'Electricity Bill Image',

        }
