from django.db import models
from datetime import datetime

class TargetFile(models.Model):
    file_name = models.CharField('File name to search and delete', max_length=200, unique=True)
    doc_url = models.CharField('URL to the webpage that explains why this file should be deleted', max_length=200)
    pub_date = models.DateTimeField('Date this file was added to the target list', default=datetime.now)

class GithubRepo(models.Model):
    scan_date = models.DateTimeField('The date this match was found', default=datetime.now)
    look_for_file = models.ForeignKey(TargetFile, on_delete=models.CASCADE)
    github_username = models.CharField('github username', max_length=200)
    github_repo = models.CharField('github repo', max_length=200)
    class Meta:
        unique_together = (("scan_date", "look_for_file"),("scan_date", "github_username"),("scan_date", "github_repo"))
