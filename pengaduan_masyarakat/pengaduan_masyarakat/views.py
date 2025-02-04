from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Mengarah ke template home.html
