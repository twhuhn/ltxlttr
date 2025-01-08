import json
from django.shortcuts import render, redirect
from .forms import LatexLetterForm

# Create your views here.
def home(request):
    form = LatexLetterForm()
    message = ""
    print(request)
    if request.method == "POST":
        form = LatexLetterForm(request.POST)
        valid = form.is_valid()
        print(valid)
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
