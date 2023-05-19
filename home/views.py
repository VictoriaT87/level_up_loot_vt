from django.shortcuts import render

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
    """
    Contact Page and Form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("thank-you"))
        else:
            messages.error(
                request,
                "Failed to send message. Please try again. All fields are required.",
            )

    form = ContactForm()
    context = {"form": form}
    return render(request, "home/contact.html", context)


def contact_thank_you(request):
    """
    Conact Thank You Page
    """
    return render(request, "home/contact_thank_you.html")