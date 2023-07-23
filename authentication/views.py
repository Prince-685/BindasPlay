<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt
import pyrebase

Config1 = {
  "apiKey": "AIzaSyBE8thS3U1OK6ALzc5bPBe1P_KprxYHVKw",
  "authDomain": "bindasplay-cb08d.firebaseapp.com",
  "databaseURL": "https://bindasplay-cb08d-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-cb08d",
  "storageBucket": "bindasplay-cb08d.appspot.com",
  "messagingSenderId": "374562043128",
  "appId": "1:374562043128:web:b3e70f1c0256afe407b70d",
  "measurementId": "G-67NLCESH35"
}
# Config2 = {
#   "apiKey": "AIzaSyBE8thS3U1OK6ALzc5bPBe1P_KprxYHVKw",
#   "authDomain": "bindasplay-cb08d.firebaseapp.com",
#   "databaseURL": "https://bindasplay-cb08d-default-rtdb.firebaseio.com",
#   "projectId": "bindasplay-cb08d",
#   "storageBucket": "bindasplay-cb08d.appspot.com",
#   "messagingSenderId": "374562043128",
#   "appId": "1:374562043128:web:b3e70f1c0256afe407b70d",
#   "measurementId": "G-67NLCESH35"
# }


Config2 = {
  "apiKey": "AIzaSyBuypl8nEeB0NbRdu3Nt2_6h3gYVPZvcHE",
  "authDomain": "bindasplay-43d58.firebaseapp.com",
  "databaseURL":"https://bindasplay-43d58-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-43d58",
  "storageBucket": "bindasplay-43d58.appspot.com",
  "messagingSenderId": "566594345888",
  "appId": "1:566594345888:web:7cb38cbcfeca0d22d622c5",
  "measurementId": "G-T3LLGYGPT2"
}

firebase1 = pyrebase.initialize_app(Config1)
authe1 = firebase1.auth()
db1 = firebase1.database()

firebase2 = pyrebase.initialize_app(Config2)
authe2 = firebase1.auth()
db2 = firebase1.database()


def checkUserCredentials(username,password):
  data = db1.child("users").get()

  credentials = []
  for x in data.each():
      info = []
      key = x.key()
      value = x.val()
      credentials.append
      print(key,value)
      if username == key and password == value:
         return True
  return False


@xframe_options_exempt
def userLogin(request):   
  try: 
    data1 = db2.child('btn1').child('b1').get()
    btn1=data1.val()
    data2 = db2.child('btn2').child('b2').get()
    btn2=data2.val()
    data3= db2.child('btn3').child('b3').get()
    btn3=data3.val()

    d1 = db2.child('kBtn1').child('b1').get()
    b1=d1.val()
    d2 = db2.child('kBtn2').child('b2').get()
    b2=d2.val()
    d3= db2.child('kBtn3').child('b3').get()
    b3=d3.val()
    
    username = request.GET['username']
    passw = request.GET['pass1'] 
    
    auth = checkUserCredentials(username,passw)

    if auth :
        if "bindas" in username:
          return render(request, "dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":btn3})
        elif "kalyan" in username:
           return render(request, "kalyandasboard.html",{"b1":b1,"b2":b2,"b3":b3})
    else:
      return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
  except Exception as e:
    print('errr--',e)
    return render(request, "Userinterface.html")
        
  

=======
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt
import pyrebase

Config = {
  "apiKey": "AIzaSyBuypl8nEeB0NbRdu3Nt2_6h3gYVPZvcHE",
  "authDomain": "bindasplay-43d58.firebaseapp.com",
  "databaseURL":"https://bindasplay-43d58-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-43d58",
  "storageBucket": "bindasplay-43d58.appspot.com",
  "messagingSenderId": "566594345888",
  "appId": "1:566594345888:web:7cb38cbcfeca0d22d622c5",
  "measurementId": "G-T3LLGYGPT2"
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()

@xframe_options_exempt
def login(request):
   
  try: 
    data1 = db.child('btn1').child('b1').get()
    btn1=data1.val()
    data2 = db.child('btn2').child('b2').get()
    btn2=data2.val()
    data3= db.child('btn3').child('b3').get()
    btn3=data3.val()

    d1 = db.child('kBtn1').child('b1').get()
    b1=d1.val()
    d2 = db.child('kBtn2').child('b2').get()
    b2=d2.val()
    d3= db.child('kBtn3').child('b3').get()
    b3=d3.val()

    if request.method == 'POST': 
        username = request.POST['username']
        pass1 = request.POST['pass1']  
        if "bindas" in username :
          p = authenticate(username=username, password=pass1)
          if p is not None:
              login_auth(request, p)
              # messages.success(request, "Logged In Sucessfully!!") 
              return render(request, "dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":btn3})
          else:
              #messages.error(request, "Wrong email id or Password")
              return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
        elif "kalyan" in username:
          p = authenticate(username=username, password=pass1)
          if p is not None:
              login_auth(request, p)
              # messages.success(request, "Logged In Sucessfully!!") 
              return render(request, "kalyandasboard.html",{"b1":b1,"b2":b2,"b3":b3})
          else:
              #messages.error(request, "Wrong email id or Password")
              return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
        else:
              #messages.error(request, "Wrong email id or Password")
          return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
        
  except Exception as e:
    print('errr--',e)
    return render(request, "Userinterface.html")

>>>>>>> bef1a1313f76ef3f7c82ced7344ab96c8179d76c
