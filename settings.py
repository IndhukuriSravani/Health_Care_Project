AUTH_USER_MODEL = 'core.User'

INSTALLED_APPS = [
    ...
    'core',
    'crispy_forms',
    ...
]

LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('te', 'Telugu'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += ['rest_framework', 'rest_framework.authtoken', 'drf_yasg']
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication']}


