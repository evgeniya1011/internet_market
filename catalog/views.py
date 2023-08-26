from django.shortcuts import render
import json

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ph_number = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'Новое сообщение от  {name}({ph_number}): {message}')
    return render(request, 'catalog/contacts.html')
