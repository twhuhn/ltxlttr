from django.shortcuts import render
from .forms import ContactForm

currentview = ''

# Create your views here.
def home(request):
    global currentview
    newview = request.GET.get('currentview', 'sender')
    currentview = newview
    return render(request, 'letterui/index.html', {'currentview': currentview})

def contact_view(request):
    form = ContactForm()
    message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "Form submitted successfully!"
            print(form.cleaned_data)
            form = ContactForm()  # Reset the form after submission

    return render(request, "letterui/contact.html", {"form": form, "message": message})
