from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {
        'categories': category_list,
    }

    return render(request, 'polls/index.html', context=context_dict)


def about(request):
    context_dict = {
        'boldmessage': "Ignorance!",
    }
    return render(request, 'polls/about.html', context=context_dict)


def just(request):
    return HttpResponse("Just?! <br> <a href='/polls/'>Home</a>")
