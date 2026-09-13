from django.shortcuts import render
from django.contrib import messages
from random import randrange
import pyrebase
import datetime





Config2 = {
    "apiKey": "AIzaSyAtIC6ftAQWnNBsFA4GYR2O9UFOPs_xsyQ",
    "authDomain": "bindasplay2-cf89e.firebaseapp.com",
    "databaseURL": "https://bindasplay2-cf89e-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "bindasplay2-cf89e",
    "storageBucket": "bindasplay2-cf89e.firebasestorage.app",
    "messagingSenderId": "394811528969",
    "appId": "1:394811528969:web:6280f4a4a76af90bdfe5d8",
    "measurementId": "G-6GCS2XMYNN"
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
        #print(x.key())
        info.append(x.key())
        info.append(x.val())
        rows.append(info)
    return render(request, "usersData.html",{'rows':rows,'gname':gname})