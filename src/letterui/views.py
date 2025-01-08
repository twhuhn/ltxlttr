from django.shortcuts import render
from .forms import LatexLetterForm
from .templating import generate_letter_template
import os
import uuid

# Create your views here.
def home(request):
    form = LatexLetterForm()
    message = ""

    if request.method == "POST":
        form = LatexLetterForm(request.POST)
        if form.is_valid():
            message = "Form submitted successfully!"
            print(form.cleaned_data)
            message = generate_letter_template(form)
            outfile = create_pdf(message)


            form = LatexLetterForm()  # Reset the form after submission

    return render(request, "letterui/index.html", {"form": form, "message": message})

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