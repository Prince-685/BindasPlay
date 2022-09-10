from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt


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
            return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
    
    
  except Exception as e:
    print('errr--',e)
    return render(request, "Userinterface.html")