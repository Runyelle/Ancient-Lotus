from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        return render(request, 'contact_success.html')  # Optional thank-you page

    return render(request, 'contact_form.html')