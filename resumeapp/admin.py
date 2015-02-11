# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
import hashlib

from .models.users import User
from resume.settings import SALT_KEY


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email')

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput()

    def save_model(self, request, obj, form, change):
        super(UserForm, self).save_model(request, obj, form, change)
        data = self.cleaned_data
        data['password'] += SALT_KEY
        password = hashlib.sha224(data['password']).hexdigest()

        User.objects.filter(login=data['login']).update(
            password1=password,
            experience_summary = data['experience_summary'],
            technical_skills = data['technical_skills'],
            work_experience = data['work_experience'],
            education = data['education'],
            personal_skills = data['personal_skills'],
            languages = data['languages']
            )
        obj.save()


class UserAdmin(admin.ModelAdmin):
    form = UserForm

    fields = (
        ('first_name', 'last_name'),
        'login', 'password', 'email',
        'birthday', 'mphone', 'photo',
        'experience_summary', 'technical_skills',
        'work_experience', 'education', 'personal_skills',
        'languages'
    )

    list_display = ('first_name', 'last_name', 'login', 'email', 'photo')


admin.site.register(User, UserAdmin)
