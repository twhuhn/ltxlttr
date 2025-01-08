from django.shortcuts import render
from .forms import LatexLetterForm

# Create your views here.
def home(request):
    form = LatexLetterForm()
    message = ""

    if request.method == "POST":
        form = LatexLetterForm(request.POST)
        if form.is_valid():
            message = "Form submitted successfully!"
            print(form.cleaned_data)
            form = LatexLetterForm()  # Reset the form after submission

    return render(request, "letterui/index.html", {"form": form, "message": message})
