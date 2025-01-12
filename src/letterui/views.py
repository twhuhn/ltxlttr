from django.shortcuts import render, redirect
from .forms import LatexLetterForm
from .pdfhandler.pdfhandler import create_pdf, generate_letter_template
import os
import uuid
import json
from django.http import HttpResponse
from datetime import datetime

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
        print(form.errors)
        if form.is_valid():
            message = "Form submitted successfully!"
            print(message)
            print(form.cleaned_data)
            response = render(request, "letterui/index.html", {"form": form, "message": message})
            response.set_cookie('content', json.dumps(form.cleaned_data))
            #return response
            message = generate_letter_template(form)
            outfile = create_pdf(message)
            with open(outfile, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                response['Content-Disposition'] = f'inline; filename={timestamp}.pdf'
                return response
            form = LatexLetterForm()  # Reset the form after submission

    return render(request, "letterui/index.html", {"form": form, "message": message})

def create_pdf(message):
    # Create a PDF file
    # Create a temporary folder with a UUID as its name
    temp_folder = os.path.join("/tmp/ltxlttr", str(uuid.uuid4()))
    os.makedirs(temp_folder, exist_ok=False) # @TODO try catch

    # Create a file input.tex in this folder with message as content
    tex_file_path = os.path.join(temp_folder, "input.tex")
    pdf_file_path = os.path.join(temp_folder, "input.pdf")
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(message)

    # Run pdflatex on this file
    os.system(f"pdflatex -output-directory={temp_folder} {tex_file_path}")
    return pdf_file_path

def clear(request):
    response = redirect('/')
    content_cookie = request.COOKIES.get('content')
    if content_cookie:
        response.delete_cookie('content')
    
    return response
