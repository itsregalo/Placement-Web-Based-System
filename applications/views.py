
from django.shortcuts import render

from applications.models import Application
from attachments.models import Attachment
from users.models import Account

# Create your views here.
def apply(request,attachment_id):
    if request.method == "POST":
        print(request.user.id)
        app = Account.objects.get(id=request.user.id)

        for attacments in Attachment.objects.filter(id=attachment_id):
            org = Account.objects.get(id=attacments.user.id)
            print("Org",org)

        attachment_id = Attachment.objects.get(id=attachment_id)
        attachment = attachment_id
        print(org)
        cv = request.POST.get('cv')
        print(cv)
        status = "Pending"
        print(status)

        applic = Application(
        organization = org,
        attachment = attachment,
        status = status,
        applicant = app,
        cv = cv
        )
        print("Saved")
        applic.save()

    return render(request,'apply.html')

def cv(request,applicant_id):
    if request.method == "POST":
        status = request.POST.get('status')
        message = request.POST.get('message')
        print(message)
        print(status)
        print(applicant_id)
        Application.objects.filter(id=applicant_id).update(
            message=message,
            status = status
        )
    #Filter Fo message response
    return render(request,'cv.html')

def app_feed_back(request):
    application = Application.objects.filter(applicant_id=request.user.id)
    data = {
      "application" : application
    }
    return render(request,'apllication_feedbacks.html',data)