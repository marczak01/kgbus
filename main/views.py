from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailContactForm

def index(request):
    sent = False
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Nowa wiadomość od: {cd['email']}"
            message = f"{ cd['message']}\nNumer telefonu: {cd['phone']}"
            send_mail(subject, message, cd['email'], ['marekmarczak25@gmail.com',] )
            sent = True
    else:
        form = EmailContactForm()
    return render(request,
                  'main/index.html',
                  {'form': form,
                   'sent': sent})