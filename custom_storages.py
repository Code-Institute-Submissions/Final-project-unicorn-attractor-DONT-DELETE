from django.conf import settings
from storages.backends.s3boto3 import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES

class PhotoStorage(S3BotoStorage):
    location = settings.PHOTOSFILES_LOCATION