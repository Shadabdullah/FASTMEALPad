from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout

def landingPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username= username , password =password)
        if user is not None:
            login(request, user)
            print(user)
            return redirect('/')
        else:
            print('Invalid')

  
    return render(request , 'base/pages/home.html')