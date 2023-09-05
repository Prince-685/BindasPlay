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


def userData(request):
    uData = db1.child("users").get()
    rows = []
    for x in uData.each():
        info = []
        print(x.key())
        info.append(x.key())
        info.append(x.val())
        rows.append(info)
    return render(request, "usersData.html",{'rows':rows})