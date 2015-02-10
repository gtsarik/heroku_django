# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from .models.users import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email')

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput()


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
