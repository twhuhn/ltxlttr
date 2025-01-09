import json
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import LatexLetterForm

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
        valid = form.is_valid()
        if valid:
            message = "Form submitted successfully!"
            
            print(form.cleaned_data)

            # Save the current content as a cookie
            response = render(request, "letterui/index.html", {"form": form, "message": message})
            response.set_cookie('content', json.dumps(form.cleaned_data))
            return response

    return render(request, "letterui/index.html", {"form": form, "message": message})

def clear(request):
    response = redirect('/')
    content_cookie = request.COOKIES.get('content')
    if content_cookie:
        response.delete_cookie('content')
    
    return response
