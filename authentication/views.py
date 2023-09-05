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

Config3 = {
  "apiKey": "AIzaSyDxFBqlyY2_eNGJRNyya4F0lS8vR4ArCrM",
  "authDomain": "milan-71cf2.firebaseapp.com",
  "databaseURL":"https://milan-71cf2-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "milan-71cf2",
  "storageBucket": "milan-71cf2.appspot.com",
  "messagingSenderId": "908285293971",
  "appId": "1:908285293971:web:cbf52f52b75f5afc846466"
}


firebase3=pyrebase.initialize_app(Config3)
auth=firebase3.auth()
db3=firebase3.database()


def checkUserCredentials(username,password):
  data = db1.child("users").get()
  # data2=db1.child("admin").get()
  # for x in data2:
  #    key=x.key()
  #    value=x.val()
  #    if username==key and password==value:
  #       return True
  credentials = []
  for x in data.each():
      info = []
      key = x.key()
      value = x.val()
      credentials.append
      # print(key,value)
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
    
    username = request.POST['username']
    passw = request.POST['pass1'] 
    
    auth = checkUserCredentials(username,passw)

    if auth :
        if "bindas" in username:
          request.session['current_username'] = username
          request.session['current_password'] = passw
          return render(request, "dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":btn3})
        elif "kalyan" in username:
           request.session['current_username'] = username
           request.session['current_password'] = passw
           return render(request, "kalyandasboard.html",{"b1":b1,"b2":b2,"b3":b3})
      
        elif "milan1" in username:
           request.session['current_username'] = username
           request.session['current_password'] = passw
           g1=db3.child('Gname').child('G1').child('G1').get().val()
           row=[g1]
           return render(request, "Userpaneldashboard.html",{'row':row})
        elif "milan2" in username:
           request.session['current_username'] = username
           request.session['current_password'] = passw
           g2=db3.child('Gname').child('G2').child('G2').get().val()
           row=[g2]
           return render(request, "Userpanel2dashboard.html",{'row':row})
    else:
      return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
  except Exception as e:
    print('errr--',e)
    return render(request, "Userinterface.html")
        
  

