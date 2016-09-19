from django.db import models
from datetime import datetime

class TargetFile(models.Model):
    file_name = models.CharField('File name to search and delete', max_length=200, primary_key=True)
    doc_url = models.CharField('URL for the webpage that explains why this file should be deleted', max_length=200)
    pub_date = models.DateTimeField('date this file name started being targeted', default=datetime.now)

class GitHub_repo(models.Model):
    scan_date = models.DateTimeField('date match found', default=datetime.now)
    look_for_file = models.ForeignKey(TargetFile, on_delete=models.CASCADE)
    github_username = models.CharField('github username', max_length=200)
    github_repo = models.CharField('github repo', max_length=200)
    # votes = models.IntegerField(default=0)
    # pub_date = models.DateTimeField('date published')
    class Meta:
        unique_together = (("scan_date", "look_for_file"),("scan_date", "github_username"),("scan_date", "github_repo"))