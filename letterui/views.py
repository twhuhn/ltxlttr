from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'letterui/index.html')

def contact_view(request):
    form = ContactForm()
    message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "Form submitted successfully!"
            form = ContactForm()  # Reset the form after submission

    return render(request, "letterui/contact.html", {"form": form, "message": message})
