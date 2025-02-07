from django.shortcuts import render

# Create your views here.


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} ({phone}) {message}')

    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
