from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'college', 'email', 'mobile', 'resume']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'college': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your college name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile number'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            file_extension = resume.name.split('.')[-1].lower()
            allowed_extensions = ['pdf', 'doc', 'docx']
            if file_extension not in allowed_extensions:
                raise forms.ValidationError(
                    'Invalid file format. Only PDF, DOC, and DOCX files are allowed.'
                )
            if resume.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError(
                    'The file is too large. Maximum file size allowed is 5MB.'
                )
        return resume