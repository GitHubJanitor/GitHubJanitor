from django.contrib import admin

# Register your models here.
from .models import TargetFile
from .models import GithubRepo

admin.site.register(TargetFile)
admin.site.register(GithubRepo)
