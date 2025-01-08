from django.shortcuts import render
from .forms import ContactForm
from .templating import generate_letter_template
import os
import uuid

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
            outfile = create_pdf(message)



            form = ContactForm()  # Reset the form after submission

    return render(request, "letterui/contact.html", {"form": form, "message": message})

def create_pdf(message):
    # Create a PDF file
    # Create a temporary folder with a UUID as its name
    temp_folder = os.path.join("/tmp", str(uuid.uuid4()))
    os.makedirs(temp_folder, exist_ok=False)

    # Create a file input.tex in this folder with message as content
    tex_file_path = os.path.join(temp_folder, "input.tex")
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(message)

    # Run pdflatex on this file
    os.system(f"pdflatex -output-directory={temp_folder} {tex_file_path}")
    return tex_file_path
    pass