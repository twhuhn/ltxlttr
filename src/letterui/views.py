from django.shortcuts import render, redirect
from .forms import LatexLetterForm
from .templating import generate_letter_template
import os
import uuid
import json

# Create your views here.
def home(request):
    message = ""
    form = LatexLetterForm()

    content_cookie = request.COOKIES.get('content')
    if content_cookie:
        # Try to parse the cookie as json. If it fails, clear the cookie and return an
        # empty form.
        try:
            content_cookie_parsed = json.loads(content_cookie)
        except:
            clear(request)
        
        form = LatexLetterForm(data=content_cookie_parsed)

    if request.method == "POST":
        form = LatexLetterForm(request.POST)
        if form.is_valid():
            message = "Form submitted successfully!"
            print(form.cleaned_data)
            response = render(request, "letterui/index.html", {"form": form, "message": message})
            response.set_cookie('content', json.dumps(form.cleaned_data))
            return response
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

def clear(request):
    response = redirect('/')
    content_cookie = request.COOKIES.get('content')
    if content_cookie:
        response.delete_cookie('content')
    
    return response