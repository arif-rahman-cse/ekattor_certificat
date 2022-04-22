from django.contrib.auth.models import User
from django import forms

from GeoCodeBD.models import Division, District, Upazila, Union
from user_entry.models import UserEntry

division_list = [('', 'Select Division'), ]
temp_division_list = Division.objects.all().values_list('id', 'name')
for division in temp_division_list:
    division_list.append(division)


class UserEntryCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Preset Address
        present_division = self.data.get('present_division')
        present_district = self.data.get('present_district')
        present_upazila = self.data.get('present_thana')

        if present_division:
            self.fields['present_district'].queryset = District.objects.filter(division=present_division)
        else:
            self.fields['present_district'].queryset = District.objects.none()

        if present_district:
            self.fields['present_thana'].queryset = Upazila.objects.filter(district=present_district)
        else:
            self.fields['present_thana'].queryset = Upazila.objects.none()

        if present_upazila:
            self.fields['present_post_office'].queryset = Union.objects.filter(upazila=present_upazila)
        else:
            self.fields['present_post_office'].queryset = Union.objects.none()

        # Permanent Address
        permanent_division = self.data.get('permanent_division')
        permanent_district = self.data.get('permanent_district')
        permanent_thana = self.data.get('permanent_thana')

        if permanent_division:
            self.fields['permanent_district'].queryset = District.objects.filter(division=permanent_division)
        else:
            self.fields['permanent_district'].queryset = District.objects.none()

        if permanent_district:
            self.fields['permanent_thana'].queryset = Upazila.objects.filter(district=permanent_district)
        else:
            self.fields['permanent_thana'].queryset = Upazila.objects.none()

        if permanent_thana:
            self.fields['permanent_post_office'].queryset = Union.objects.filter(upazila=permanent_thana)
        else:
            self.fields['permanent_post_office'].queryset = Union.objects.none()

    class Meta:
        model = UserEntry
        fields = (
            'name_en', 'name_bn', 'care_of', 'care_of_name_en', 'care_of_name_bn', 'mother_name_en', 'mother_name_bn',
            'email', 'phone', 'date_of_birth', 'gender', 'blood_group', 'nid_no', 'birth_reg_no', 'present_address_en',
            'present_address_bn', 'present_area_village_en', 'present_area_village_bn', 'present_division',
            'present_district',
            'present_thana', 'present_post_office', 'present_post_code', 'residence_status',
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
            'present_division': forms.Select(attrs={'class': 'form-control'}, choices=division_list),
            'present_district': forms.Select(attrs={'class': 'form-control'}, ),
            'present_thana': forms.Select(attrs={'class': 'form-control'}),
            'present_post_office': forms.Select(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),
            'present_post_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'residence_status': forms.Select(attrs={'class': 'form-control'}),

            # Permanent Address
            'permanent_address_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_address_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_division': forms.Select(attrs={'class': 'form-control'}, choices=division_list),
            'permanent_district': forms.Select(attrs={'class': 'form-control'}),
            'permanent_thana': forms.Select(attrs={'class': 'form-control'}),
            'permanent_post_office': forms.Select(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),
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


class UserEntryUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Preset Address
        present_division = self.data.get('present_division') or self.instance.present_division.id
        present_district = self.data.get('present_district') or self.instance.present_district.id
        present_upazila = self.data.get('present_thana') or self.instance.present_thana.id

        self.fields['present_district'].queryset = District.objects.filter(division=present_division)
        self.fields['present_thana'].queryset = Upazila.objects.filter(district=present_district)
        self.fields['present_post_office'].queryset = Union.objects.filter(upazila=present_upazila)

        # Permanent Address
        permanent_division = self.data.get('permanent_division') or self.instance.permanent_division.id
        permanent_district = self.data.get('permanent_district') or self.instance.permanent_district.id
        permanent_thana = self.data.get('permanent_thana') or self.instance.permanent_thana.id

        self.fields['permanent_district'].queryset = District.objects.filter(division=permanent_division)
        self.fields['permanent_thana'].queryset = Upazila.objects.filter(district=permanent_district)
        self.fields['permanent_post_office'].queryset = Union.objects.filter(upazila=permanent_thana)

    class Meta:
        model = UserEntry
        fields = (
            'name_en', 'name_bn', 'care_of', 'care_of_name_en', 'care_of_name_bn', 'mother_name_en', 'mother_name_bn',
            'email', 'phone', 'date_of_birth', 'gender', 'blood_group', 'nid_no', 'birth_reg_no', 'present_address_en',
            'present_address_bn', 'present_area_village_en', 'present_area_village_bn', 'present_division',
            'present_district',
            'present_thana', 'present_post_office', 'present_post_code', 'residence_status',
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
            'present_division': forms.Select(attrs={'class': 'form-control'}, choices=division_list),
            'present_district': forms.Select(attrs={'class': 'form-control'}, ),
            'present_thana': forms.Select(attrs={'class': 'form-control'}),
            'present_post_office': forms.Select(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),
            'present_post_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'residence_status': forms.Select(attrs={'class': 'form-control'}),

            # Permanent Address
            'permanent_address_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_address_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_area_village_bn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'permanent_division': forms.Select(attrs={'class': 'form-control'}, choices=division_list),
            'permanent_district': forms.Select(attrs={'class': 'form-control'}),
            'permanent_thana': forms.Select(attrs={'class': 'form-control'}),
            'permanent_post_office': forms.Select(attrs={'required': True, 'class': 'form-control', 'placeholder': ''}),
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
