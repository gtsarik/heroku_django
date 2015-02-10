import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        # 'NAME': 'resume_db',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'HOST': 'ec2-174-129-213-103.compute-1.amazonaws.com',
        'USER': 'rbfrtnwxyfgtfn',
        'PASSWORD': 'Fd-_Va27VPHTumBqecpZc3IyIY',
        'NAME': 'd6o2soljsnsmmk',
    }
}

DEBUG = True
