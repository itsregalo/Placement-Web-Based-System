from unicodedata import name
from django.shortcuts import render
from applications.models import Application
from attachments.models import Attachment

from tags.models import Tag

# Create your views here.
def attachments_create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    print(title)
    print(description)

    #split tag string into list of tags form sentence

    #save attacment to DB try and except
    try:
        attachment = Attachment(
            title = title,
            description = description,
            user_id = request.user.id
        )
        attachment.save()
        print("attachment saved")
    except:
        print("attachment not saved")
    return render(request,'create_attachment.html')

def list_attachments(request):
    #filter attacments with user_id
    attachments = Attachment.objects.filter(user_id=request.user.id).order_by('-id')
    # paginate the attachments 

    return render(request,'list_attachments.html',{'attachments':attachments})

#attacment detail to view all the applicant on a single attacment
def attachment_application_detail(request,attachment_id):
    applicant = Application.objects.filter(attachment=attachment_id)
    for app in applicant:
        print(app.id)
    return render(request,'attachment_detail.html',{'applications':applicant})
    





