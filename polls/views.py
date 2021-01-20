from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",
                    'link_to_just': "/polls/just",
                    }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'polls/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says hey there partner! <br> <a href='/polls/'>Home</a>")


def just(request):
    return HttpResponse("Just?! <br> <a href='/polls/'>Home</a>")
