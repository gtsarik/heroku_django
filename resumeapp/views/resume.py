# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages

from ..models.users import User


def resume_list(request):
    experience = [
        'EXPERIENCE SUMMARY:',
        'DEVELOPERS and TECHNICAL SKILLS:',
        'WORK EXPERIENCE:',
        'EDUCATION and TRAINING:',
        'PERSONAL SKILLS:',
        'LANGUAGES:'
    ]
    experience_summary = []
    technical_skills = []
    work_experience = []
    education = []
    personal_skills = []
    languages = []
    current_user = []
    error_message = u'В базе данных нет ни одного пользователя'

    try:
        user_log = request.session['user_log']

        if user_log:
            current_user = User.objects.get(login=user_log)
        else:
            current_user = User.objects.get(login='gtsarik')

        if current_user.experience_summary:
            experience_summary = current_user.experience_summary.split(';')

        if current_user.technical_skills:
            technical_skills = current_user.technical_skills.split(';')

        if current_user.work_experience:
            work_experience = current_user.work_experience.split(';')

        if current_user.education:
            education = current_user.education.split(';')

        if current_user.personal_skills:
            personal_skills = current_user.personal_skills.split(';')

        if current_user.languages:
            languages = current_user.languages.split(';')
    except Exception:
        messages.error(request, error_message, extra_tags='warning')

    return render(request, 'resume/index.html',
        {'current_user': current_user,
        'experience_summary': experience_summary,
        'technical_skills': technical_skills,
        'work_experience': work_experience,
        'education': education,
        'personal_skills': personal_skills,
        'languages': languages,
        'experience': experience}
    )
