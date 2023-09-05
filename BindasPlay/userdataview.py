from django.shortcuts import render
from django.contrib import messages
from random import randrange
import pyrebase
import datetime





Config2 = {
  "apiKey": "AIzaSyBE8thS3U1OK6ALzc5bPBe1P_KprxYHVKw",
  "authDomain": "bindasplay-cb08d.firebaseapp.com",
  "databaseURL": "https://bindasplay-cb08d-default-rtdb.firebaseio.com",
  "projectId": "bindasplay-cb08d",
  "storageBucket": "bindasplay-cb08d.appspot.com",
  "messagingSenderId": "374562043128",
  "appId": "1:374562043128:web:b3e70f1c0256afe407b70d",
  "measurementId": "G-67NLCESH35"
}

firebase1 = pyrebase.initialize_app(Config2)
auth = firebase1.auth()
db1 = firebase1.database()

Config3 = {
  "apiKey": "AIzaSyDxFBqlyY2_eNGJRNyya4F0lS8vR4ArCrM",
  "authDomain": "milan-71cf2.firebaseapp.com",
  "databaseURL":"https://milan-71cf2-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "milan-71cf2",
  "storageBucket": "milan-71cf2.appspot.com",
  "messagingSenderId": "908285293971",
  "appId": "1:908285293971:web:cbf52f52b75f5afc846466"
}


firebase2=pyrebase.initialize_app(Config3)
authe=firebase2.auth()
db2=firebase2.database()


def userData(request):
    g1=db2.child('Gname').child('G1').child('G1').get().val()
    g2=db2.child('Gname').child('G2').child('G2').get().val()
    uData = db1.child("users").get()
    rows = []
    gname=[g1,g2]
    for x in uData.each():
        info = []
        print(x.key())
        info.append(x.key())
        info.append(x.val())
        rows.append(info)
    return render(request, "usersData.html",{'rows':rows,'gname':gname})