import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


# Create your views here.
def homePage(request):
    response = requests.get('http://127.0.0.1:8000/shopping/product/')
    product_data = response.json()
    print(product_data)
    # return render(request, 'core/home.html', {
    #     'ip': product_data['ip'],
    #     'country': geodata['country_name']
    # })
    return render(request, 'online_shopping_app/homePage.html', {"product_list":product_data})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homePage')
    else:
        form = SignUpForm()
    return render(request, 'online_shopping_app/signup.html', {'form': form})

def productdetail(request,p_id):
    api_url = 'http://127.0.0.1:8000/shopping/product/'+str(p_id)
    response = requests.get(api_url)
    product_data = response.json()
    return  render(request, 'online_shopping_app/product_detail.html',{"product":product_data})

def invoice(request):
    return render(request, 'online_shopping_app/invoice.html', {})
