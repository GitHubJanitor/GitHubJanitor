from django.contrib import admin

from .models import TargetFile
from .models import GithubRepo

admin.site.register(TargetFile)
admin.site.register(GithubRepo)
