from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.contrib import messages

from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    """
    View to return index page
    """
    return render(request, 'home/index.html')


def faqs(request):
    """
    FAQs Page
    """
    return render(request, "home/faqs.html")


def contact(request):
    """ View to return Contact Us form """
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['victoriaemt@gmail.com'])
        messages.success(request,
                         'Thank You, your email has been sent. We will contact you shortly.')
        return render(request, "home/contact.html")
    else:
        return render(request, "home/contact.html")