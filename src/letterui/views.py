import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from datetime import datetime

from .forms import LatexLetterForm
from .pdfhandler.pdfhandler import create_pdf, generate_letter_template

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
            template = generate_letter_template(form.cleaned_data)
            print(template)
            outfile = create_pdf(template)
            try:
                with open(outfile, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                    response.set_cookie('content', json.dumps(form.cleaned_data))
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    response['Content-Disposition'] = f'inline; filename={timestamp}.pdf'
                    return response  # Reset the form after submission
            except FileNotFoundError:
                return HttpResponseServerError('Failed to Create Latex File from Template\nTemplate content: ' + template)

    return render(request, "letterui/index.html", {"form": form, "message": message})

def clear(request):
    response = redirect('/')
    content_cookie = request.COOKIES.get('content')
    if content_cookie:
        response.delete_cookie('content')
    
    return response

