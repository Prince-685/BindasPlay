from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Text, TextForm


@xframe_options_exempt
def login(request):
   
  try: 
    if request.method == 'POST': 
        username = request.POST['username']
        pass1 = request.POST['pass1']  
        p = authenticate(username=username, password=pass1)
        
        if p is not None:
            login_auth(request, p)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "dasboard.html")
        else:
            #messages.error(request, "Wrong email id or Password")
            return render(request, "userinterface.html",{'msg':'Wrong Username/Password'})
    
    
  except Exception as e:
    print('errr--',e)
    return render(request, "userinterface.html")
def text_new(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            return HttpResponse('Test')
    else:
        form = TextForm()

    return render(request, 'projectname/new.html', {'form': form})