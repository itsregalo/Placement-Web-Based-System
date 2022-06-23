from django.db import models
from attachments.models import Attachment
from users.models import Account

STATUS = ((1, "Pending"), (2, "Success"), (3, "Failed"))

# Create your models here.
class Application(models.Model):
    applicant = models.ForeignKey(Account, blank=True,null=True, on_delete=models.CASCADE,related_name="applicant")
    organization = models.ForeignKey(Account, blank=True,null=True, on_delete=models.CASCADE,related_name="organization")
    attachment = models.ForeignKey(Attachment, blank=True,null=True, on_delete=models.CASCADE,related_name="attachment")
    status = models.CharField(choices=STATUS,default=1,max_length=25)
    cv = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(blank=True,null=True,max_length=25)
    message = models.CharField(blank=True,null=True,max_length=25)
    updated_at = models.DateTimeField(auto_now=True)