from django.contrib import admin

from .models import TargetFile
from .models import GitHub_repo

admin.site.register(TargetFile)
admin.site.register(GitHub_repo)