from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_content = {
        "title" : "contato",
        "text" : "Contatos lalala",
        "number" : 123456789,
        "list": [1,2,3,4,5]
    }

    return render(request, "contact.html", my_content)