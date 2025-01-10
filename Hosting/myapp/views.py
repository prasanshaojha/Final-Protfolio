from django.shortcuts import render
from .models import Content
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from myapp.form import ContactForm  # Corrected import


def home(request):
    return render(request, 'index.html')

def research_papers(request):
    papers = Content.objects.filter(content_type='RESEARCH')
    return render(request, 'paper.html', {'papers': papers})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form to the database
            form.save()
            
            # Send an email notification to the admin or the user
            subject = f"Contact Form Submission: {form.cleaned_data['full_name']}"
            message = f"Message: {form.cleaned_data['message']}\n\nFrom: {form.cleaned_data['full_name']}\nEmail: {form.cleaned_data['email']}"
            recipient_email = 'arpanacharya11.aa@gmail.com'  # Replace with the recipient email address
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
            
            # Redirect to a success page
            return redirect('contact_success')  # Assuming you have a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
