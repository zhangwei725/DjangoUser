import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'mvep26n9ryxh716)brg4roffm_jg1_nek(hw*-6k+7kkbkmq_x'
DEBUG = True
ALLOWED_HOSTS = []
# 系统内置
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 自定义的app
CUSTOM_APPS = [
    'user_auth',
    'redi',
]

EXT_APPS = [
    # 验证码
    'captcha',
]
INSTALLED_APPS = SYS_APPS + CUSTOM_APPS + EXT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 全局配置 登录跳转的url
LOGIN_URL = '/users/login/'

ROOT_URLCONF = 'DjangoUser.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoUser.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django07',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# 静态文件配置
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 用户内置用户修改
AUTH_USER_MODEL = 'user_auth.User'

# 验证码的配置信息

# 配置生成验证码图片的大小
CAPTCHA_IMAGE_SIZE = (100, 25)
CAPTCHA_LENGTH = 6  # 字符个数
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
