from django.shortcuts import render


def index(request):
    template = 'choose_phone/choose_phone.html'
    context = {'hello': 'hello'}
    return render(request, template, context)
