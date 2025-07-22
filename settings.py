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
