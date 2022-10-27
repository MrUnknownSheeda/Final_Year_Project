from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def todays_market(request):
    return render(request, 'todays_market.html')

def stock_rates(request):
    return render(request, 'stock_rates.html')

def reports(request):
    return render(request, 'reports.html')

def main(request):
    return render(request, 'main.html')
