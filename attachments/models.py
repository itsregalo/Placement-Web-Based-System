from tags.models import Tag
from django.db import models

STATUS = ((1, True), (0, False),)

class Attachment(models.Model):
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(choices=STATUS,default=0,max_length=25)
    description =  models.CharField(max_length=255,null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

