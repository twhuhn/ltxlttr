from django.shortcuts import render
from .forms import ContactForm
from .templating import generate_letter_template

# Create your views here.
def home(request):
    return render(request, 'letterui/index.html')

def contact_view(request):
    form = ContactForm()
    message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = generate_letter_template(form)
            form = ContactForm()  # Reset the form after submission

    return render(request, "letterui/contact.html", {"form": form, "message": message})
